
// $('h1').css('background-color','green')

//     $('#btn1').on('click',()=>{
//         $('h1').css({'background-color':'red',
//             'font-size':'10rem'
    
//     })
//     })


const newImage=$('#pic1')
const sendBtn=$('#btn1')

sendBtn.on('click',()=>{
    newImage.fadeOut(2000).fadeIn(2000)
})