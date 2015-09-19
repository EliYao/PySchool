$(function(){
  $("#add_box button").click(function(){
    $('#add_box').fadeOut();
  });
  $('#add_btn').click(function(){
    $('#add_box').fadeIn();
  });
  
  $('#btn_submit').click(function(){
    var $keyVal = $("#text_submit").val();
    var t = new Date();
    var year = t.getFullYear();
    var month = t.getMonth();
    var date = t.getDate();
    var hour = t.getHours();
    var minute = t.getMinutes();
    var second =  t.getSeconds();
    var nowTime = year + "-" + month + "-" + date +" " + hour +":" + minute + ":" + second;
    if($keyVal == undefined || $keyVal == "" || $keyVal == null){
      alert("请填写内容后再提交");
    } else{
      var $userName = $("#UserName").text();
      console.log($userName);
      var $getImg = $(".add-comment img").val();
      var $insertLi = "<li class='comments'>"+"<img src='school/images/Compilers_principles.png' />"+"<div class='comments-detail'><h4>" + $userName + "</h4><div class='comments-time'>"+ nowTime +"</div><p>"+ $keyVal +"</p></div></li>";
      $("#comment-warp").append($insertLi);
    }
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

