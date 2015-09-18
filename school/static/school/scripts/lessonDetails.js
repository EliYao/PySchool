$(function(){
  $('#btn_submit').click(function(){
    var $keyVal = $("#text_submit").val();
    var mydate = new Date();
    var t = mydate.toLocaleString();
    if($keyVal == undefined || $keyVal == "" || $keyVal == null){
      alert("请填写内容后再提交");
    } else{
      var $userName = $(".add-comment-detail h4").val();
      var $getImg = $(".add-comment img").val();
      var $insertLi = "<li class='comments'>"+"<img src='school/images/Compilers_principles.png' />"+"<div class='comments-detail'><h4>" + $userName + "</h4><div class='comments-time'>"+ t +"</div>"+ $keyVal +"</p></div></li>";
      
      $("#comment-warp").append($insertLi);
    }
  
  $('.comments').click(function(){
  if ($(this).hasClass("comments-click")){
    $(this).removeClass("comments-click");
  } else {
    $(this).addClass("comments-click");
    $(this).siblings().removeClass("comments-click");
  }
  });
  });
});

$(document).ready(function(){
  $('.comments').click(function(){
  if ($(this).hasClass("comments-click")){
    $(this).removeClass("comments-click");
  } else {
    $(this).addClass("comments-click");
    $(this).siblings().removeClass("comments-click");
  }
  });
});