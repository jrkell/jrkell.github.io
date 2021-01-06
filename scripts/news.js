const num_headlines = 10;
const max_chars = 90;

const getRedditContent = (subreddit, divName) => {
    let news_content = `<h2>/r/${subreddit}</h2><ul>`;
    let news_request = new XMLHttpRequest();
    news_request.open("GET", `https://www.reddit.com/r/${subreddit}/.json`);
    news_request.send();
    news_request.onload = () => {
        news_items = JSON.parse(news_request.response).data.children;
        console.log(news_items);
        for (let i=0; i < num_headlines; i++) {
        // news_items.forEach(item => {
            item = news_items[i]
            news_content += (`<li><a href=https://old.reddit.com${item.data.permalink}>💬</a> <a href=${item.data.url}>${truncate(item.data.title)}</a></li>`);
            console.log(item.data.title)
        };
        news_content += "</ul>"
        document.getElementById(divName).innerHTML = news_content;
    }
}

const truncate = (text) => {
    if (text.length < max_chars) {
        return text;
    }
    return text.substring(0,max_chars-3) + "..."
}

getRedditContent('worldnews', 'news')
getRedditContent('australia', 'aus')