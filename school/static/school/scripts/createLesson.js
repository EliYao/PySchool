$(function(){
   var $count = $('.content-item')
   var len = $count.length;
   
   
   $("#add").click(function(){
     len++;
     var scount = len.toString();
     var k = new change(scount);
     var $content_item = "<div class='content-item'><div class='contenet-top-out'>第" + k.pri_ary() +"课时：</div><div class='content-top-in'><div class='courseName'>课程名称</div><input type='text' placeholder='输入课程名称'></input></div><div class='dropBtn'></div></div>"
   $(".content-top").append($content_item);
     len = $('.content-item').length;
     console.log(len);
   $(".dropBtn").click(function(){
    $(this).parent().remove();
    len = $('.content-item').length;
    console.log(len);
  });
});
   
   $("#add2").click(function(){
     len++;
     var scount = len.toString();
     var k = new change(scount);
     var $content_item = "<div class='content-item'><div class='contenet-top-out'>第" + k.pri_ary() +"课时：</div><div class='content-top-in'><div class='courseName'>课程名称</div><input type='text' placeholder='输入课程名称'></input></div><div class='content-top-video'><div class='courseName'>视频链接</div><input type='text' placeholder='输入视频地址'></input></div> <div class='dropBtn'></div></div>"
   $(".content-top").append($content_item);
    len = $('.content-item').length;
   $(".dropBtn").click(function(){
    $(this).parent().remove();
    len = $('.content-item').length;
    console.log(len);
  });
  });
});

