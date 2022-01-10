
$(document).ready(function () {
    bookmenu('novel');
});



function bookmenu(type) {
    let bookType = (type)
    $('.bookMenu').empty();

    $.ajax({
        type: "GET",
        url: `/book?type_give=${bookType}`,
        data: {},
        success: function (response) {
            // console.log(response['booklist']);
            let booklist = response['booklist']
            for (let i=0; i<7; i++){
                let title = booklist[i]['title']
                let img = booklist[i]['img']
                let url = booklist[i]['url']
                let writer = booklist[i]['writer']
                // console.log(title)
                let temp_html =
                `<li class="recommend-list">
                    <a href="${url}" target="_blank">
                        <img class="book-img" src="${img}" alt="recommend-book">
                        <p class="book-tit">${title}</p>
                        <p class="book-author">${writer}</p>
                    </a>
                </li> `
                $('.bookMenu').append(temp_html)
            }
        }
    })
}

