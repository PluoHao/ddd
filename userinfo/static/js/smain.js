// 轮播
var i = -1;
var time=0;
junmper();
function junmper(){
    i++;
    if(i>4)
    i=0;
    $(".nav ul li").eq(i).addClass("bg").siblings().removeClass("bg");
        $(".pic ul li").eq(i).fadeIn(100).siblings().fadeOut(100);
        $(".pic ul li").eq(i).find(".img1").css({left:"-760px"});
        $(".pic ul li").eq(i).find(".img2").css({display:"none",left:"-15px"});
        $(".pic ul li").eq(i).find(".img1").animate({left:"0px"},500,
            function(){
            $(".pic ul li").eq(i).find(".img2").css("display","block");
            $(".pic ul li").eq(i).find(".img2").animate({left:"0px"},500);
        });

        }
time=setInterval("junmper()",3700);
$(".nav ul li").click(function(){
    i=$(this).index();
    $(".nav ul li").eq(i).addClass("bg").siblings().removeClass("bg");
        $(".pic ul li").eq(i).fadeIn(100).siblings().fadeOut(100);
        $(".pic ul li").eq(i).find(".img1").css({left:"-760px"});
        $(".pic ul li").eq(i).find(".img2").css({display:"none",left:"-15px"});
        $(".pic ul li").eq(i).find(".img1").animate({left:"0px"},500,function(){
            $(".pic ul li").eq(i).find(".img2").css("display","block");
            $(".pic ul li").eq(i).find(".img2").animate({left:"0px"},500);
        });

});
$(".nav ul li").hover(function(){
    clearInterval(time);
},function(){
    time=setInterval("junmper()",3700);
});

// 全局搜索
$('#Serch').click(function () {
    alert($('#search').val())
});