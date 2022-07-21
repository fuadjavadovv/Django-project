// const readtooglef = document.querySelector(".read-more-btn");
// const readtoogleh = document.querySelector(".hidden12");
 const text1 = document.querySelectorAll(".hidden");
let test = document.getElementById("test")
console.log(test)
// console.log("safadasd")
test.addEventListener('click', (e) => {
    text1.forEach(e => e.classList.toggle("hidden"))
    
    

    if (test.innerText == "Daha cox gorset"){
        test.innerText = "Daha az gorset"
    }
    else{
        test.innerText = "Daha cox gorset"
    }
})

