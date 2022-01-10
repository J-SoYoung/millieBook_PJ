$(document).ready(function () {
    showCard();
});


function reviewCard() {
    let search= $("#book-search-url").val()
    let comment= $("#book-comment-url").val()

    $.ajax({
        type: "POST",
        url: "/search",
        data: {'search_give':search, 'comment_give':comment},
        success: function (response) { // 성공하면
           console.log(response['result']);
           window.location.reload()
        }
    })
}

function showCard() {
    $('.movie-listBox').empty();

    $.ajax({
        type: "GET",
        url: "/search",
        data: {},
        success: function (response) {
            // console.log(response["result"]);
            let book = response["result"]
            for (let i=0; i<=book.length; i++){
                let title = book[i]['title']
                let image = book[i]['image']
                let link = book[i]['link']
                let author = book[i]['author']
                let comment = book[i]['comment']
            // console.log(title, image, link)
                let temp_html = `
                <div class="review-card">
                    <a class="card-img" href="${link}">
                        <img src="${image}" alt="book">
                    </a>
                    <div class="card-text">
                        <div class="text-box">
                            <p class="text-title">${title}</p>
                            <p class="text-author">${author}</p>
                        </div>
                        <div class="review-comment">
                            <p class="comment-tit">한줄소감</p>
                            <p class="comment">${comment}</p>
                        </div>
                    </div>
                </div>`
                $('.review-saveBox').append(temp_html)
            }
        }
    })
}

