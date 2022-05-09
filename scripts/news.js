const num_headlines = 10;
const max_chars = 120;

const getRedditContent = (subreddit, contentDivName, headerDivName) => {
    const title = `<h2>/r/${subreddit}</h2>`
    let news_content = `<div><ul>`;
    let news_request = new XMLHttpRequest();
    news_request.open("GET", `https://www.reddit.com/r/${subreddit}/.json`);
    news_request.send();
    news_request.onload = () => {
        news_items = JSON.parse(news_request.response).data.children;
        // console.log(news_items);
        for (let i=0; i < num_headlines; i++) {
            item = news_items[i]
            news_content += (`<li><a href=https://old.reddit.com${item.data.permalink}>💬</a> <a href=${item.data.url}>${truncate(item.data.title)}</a></li>`);
            // console.log(item.data.title)
        };
        news_content += "</ul></div>"
        document.getElementById(headerDivName).innerHTML = title;
        document.getElementById(contentDivName).innerHTML = news_content;
    }
}

const truncate = (text) => {
    if (text.length < max_chars) {
        return text;
    }
    return text.substring(0,max_chars-3) + "..."
}

getRedditContent('worldnews', 'news', 'worldnews_header')
getRedditContent('australia', 'aus', 'aus_header')
getRedditContent('listentothis', 'listentothis', 'listentothis_header')


var coll = document.getElementsByClassName('news_header')
var i;

for (i = 0; i < coll.length; i++) {
    console.log(coll[i])
    coll[i].addEventListener("click", function() {
        console.log("you clicked bro?")
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}