import crypto from 'crypto'

let colours = { // Make it preddy
    Reset: "\x1b[0m", // Fuckin love these things
    Bright: "\x1b[1m",// I don't care if I don't need all of them.
    Dim: "\x1b[2m",   // I don't wanna delete them incase I wanna do more pretty formatting >:(
    Underscore: "\x1b[4m",
    Blink: "\x1b[5m",
    Reverse: "\x1b[7m",
    Hidden: "\x1b[8m",

    FgBlack: "\x1b[30m",
    FgRed: "\x1b[31m",
    FgGreen: "\x1b[32m",
    FgYellow: "\x1b[33m",
    FgBlue: "\x1b[34m",
    FgMagenta: "\x1b[35m",
    FgCyan: "\x1b[36m",
    FgWhite: "\x1b[37m",
    FgGray: "\x1b[90m",

    BgBlack: "\x1b[40m",
    BgRed: "\x1b[41m",
    BgGreen: "\x1b[42m",
    BgYellow: "\x1b[43m",
    BgBlue: "\x1b[44m",
    BgMagenta: "\x1b[45m",
    BgCyan: "\x1b[46m",
    BgWhite: "\x1b[47m",
    BgGray: "\x1b[100m",

}


async function get_response(seriesID, matchId, inning, over) {
    let url_full = `https://hs-consumer-api.espncricinfo.com/v1/pages/match/comments?lang=en&seriesId=${seriesID}&matchId=${matchId}&inningNumber=${inning}&commentType=ALL&sortDirection=DESC&fromInningOver=${Math.floor(1 + over / 2) * 2}`
    let exp = Math.floor(+new Date() / 1000)
    let url = encodeURIComponent(
        url_full.replace("https://hs-consumer-api.espncricinfo.com", ""))
        .replace(/[~'*]/g, (function (e) {
            return "%" + e.charCodeAt(0).toString(16)
        }))
        .replace(/%../g, (function (e) {
            return e.toLowerCase()
        }))
    const key = '9ced54a89687e1173e91c1f225fc02abf275a119fda8a41d731d2b04dac95ff5';
    const hmac = crypto.createHmac('sha256', Buffer.from(key, 'hex')).update('exp=' + exp + '~url=' + url).digest('hex');
    // console.log(hmac);

    return await fetch(url_full, {  // I love that dev-tools has the "copy as fetch" cause I would have spent *years* making typos in this bloody formatting
        "credentials": "omit",          // Also I like copying headers over incase they are checking User-Agent or something
        "headers": {                    // It is a myrical that they don't use cloudflare.
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Origin": "https://www.espncricinfo.com",
            "Referer": "https://www.espncricinfo.com",
            "x-hsci-auth-token": "exp=" + exp + "~hmac=" + hmac,    // Working out how to work out the hmac so fucking long istg
            "Sec-Fetch-Dest": "empty",                              // Like a solid 4 hours at *least*. I know I worked it out at 1:44am.
            "Sec-Fetch-Mode": "cors",                               // It was very exciting to finally get the correct hash tbf.
            "Sec-Fetch-Site": "same-site",                          // Really need to learn all the bs protocols better. Would probably have saved me like half an hour.
            "Priority": "u=4"
        },
        "referrer": "https://www.espncricinfo.com/",
        "method": "GET",
        "mode": "cors"
    })
}

function handle_html(string_) {
    if (!string_) {
        return string_
    }
    return string_.replaceAll("<B>", colours.Bright + colours.Underscore) // Using an underscore instead of bold cause bold is a little hard to see in the terminal.
        .replaceAll("<b>", colours.Bright + colours.Underscore) // Yeah, that's right, this page is (shockingly) formated in a very annoying way.
        .replaceAll("</B>", colours.Reset)
        .replaceAll("</b>", colours.Reset)
        .replaceAll("<P>", "")
        .replaceAll("<p>", "")
        .replaceAll("<pP", "") // I don't even know at this point.
        .replaceAll("<a href=", "")
        .replaceAll("target=_blank>", "")
        .replaceAll("</a>", "")
}

function print_nice(inning) { // Honestly kinda loving this ngl
    let prefix = "  - "
    if (inning.isWicket) prefix = ("  " + colours.BgRed + colours.FgWhite + "W" + colours.Reset + " ");
    if (inning.isSix) prefix = ("  " + colours.BgGreen + colours.FgWhite + "6" + colours.Reset + " ");
    if (inning.isFour) prefix = ("  " + colours.BgGreen + colours.FgWhite + "4" + colours.Reset + " ");

    if (inning.commentPreTextItems)
        inning.commentPreTextItems.reverse().forEach(function (item, index) {
            if (!item.html) {
                return
            }
            console.log(colours.Dim, handle_html(item.html).replace(colours.Reset, (colours.Reset + colours.Dim)), colours.Reset)
        });

    console.log(inning.oversActual, colours.FgBlue, handle_html(inning.title));


    if (inning.commentTextItems)
        inning.commentTextItems.reverse().forEach(function (item, index) {
            console.log(colours.Reset, prefix, handle_html(item.html))
        });

    if (inning.dismissalText) {
        console.log("    ", colours.FgRed, handle_html(inning.dismissalText.short) + ":", colours.FgBlack, colours.BgWhite, handle_html(inning.dismissalText.commentary), colours.Reset)

    }
    if (inning.commentPostTextItems)
        inning.commentPostTextItems.reverse().forEach(function (item, index) {
            console.log(colours.Dim, handle_html(item.html).replace(colours.Reset, (colours.Reset + colours.Dim)), colours.Reset)
        });


}

async function main() {
    let seriesId = process.argv[2]
    let matchId = process.argv[3]
    let inning = process.argv[4]
    let over = process.argv[5] //

    get_response(seriesId, matchId, inning, over).then((res) => res.json())
        .then((data) => {
            data.comments.reverse().forEach(function (item, index) {
                if (Math.floor(item.oversActual) == over)
                    print_nice(item);
            })
        })
}

main().then(r => {
})
