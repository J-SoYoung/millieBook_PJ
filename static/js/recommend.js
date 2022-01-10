const novelBtn = document.querySelector('.li-novel')
const humanBtn = document.querySelector('.li-humanities')
const poemBtn = document.querySelector('.li-poem')
const currentBTN = false 

novelBtn.addEventListener('click',()=>{
    novelBtn.style.backgroundColor = 'black'
    novelBtn.style.color = 'white'
    humanBtn.style.backgroundColor = 'white'
    humanBtn.style.color = 'black'
    poemBtn.style.backgroundColor = 'white'
    poemBtn.style.color = 'black'
})
humanBtn.addEventListener('click',()=>{
    humanBtn.style.backgroundColor = 'black'
    humanBtn.style.color = 'white'
    novelBtn.style.backgroundColor = 'white'
    novelBtn.style.color = 'black'
    poemBtn.style.backgroundColor = 'white'
    poemBtn.style.color = 'black'
})
poemBtn.addEventListener('click',()=>{
    poemBtn.style.backgroundColor = 'black'
    poemBtn.style.color = 'white'
    humanBtn.style.backgroundColor = 'white'
    humanBtn.style.color = 'black'
    novelBtn.style.backgroundColor = 'white'
    novelBtn.style.color = 'black'
})
