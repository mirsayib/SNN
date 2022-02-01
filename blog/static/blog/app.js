const toggleComments = () => {
    if (commentSection.classList.contains("invisible")) {
        commentSection.classList.remove("invisible")
    } else {
        commentSection.classList.add("invisible")
    }
}

var exp_comments = document.querySelector('.expand-comments')

if(exp_comments){
    exp_comments.addEventListener('click', toggleComments)
}

var commentSection = document.querySelector('.comment-section')

