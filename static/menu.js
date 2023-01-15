let menu=document.getElementById('hamburger')
menu.addEventListener("click",function(){
    document.getElementById('over').style.width="100%"
})
let close=document.getElementById('close')
close.addEventListener("click",function(){
    document.getElementById('over').style.width="0%"
})
