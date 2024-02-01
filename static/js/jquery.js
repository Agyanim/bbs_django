// $('h1').css('background-color','green')

//     $('#btn1').on('click',()=>{
//         $('h1').css({'background-color':'red',
//             'font-size':'10rem'

//     })
//     })

const newImage = $("#pic1");
const sendBtn = $("#btn1");

let count=0
sendBtn.on("click", () => {
//   newImage.toggle()
setInterval(() => {
    newImage.animate({
        left:'+=50',
        height:'toggle'
      },500)
    count +=10
    console.log(count)
    if (count>50){
        newImage.stop()
    }
}, 200);


});
newImage.on("click", () => {
    newImage.stop()
//   newImage.animate({
//     left:'+=20'
//   },500)
    
});
