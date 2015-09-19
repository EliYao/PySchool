$(function(){
   $("#createrBtn").click(function(){
     var $areaC1 = $(".c1").val();
     var $areaC2 = $(".c2").val();
     if ($areaC1 == undefined | $areaC2 == undefined){
       alert("请填写完整！");
     }
  });
});









