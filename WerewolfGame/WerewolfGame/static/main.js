
require(["jquery"],function($){
	console.log("成功引入 jquery "+$().jquery);
	
	var
	//事件处理逻辑
	EventHandler = {
		"dealLogin":function(){
			var params = {
				"username":$("#account").val(),
				"password":$("#password").val()
			};
			console.log(params);
		    $.ajax({
                cache:false,
				type:"post",
				url:"/login",
				async:true,
				data:params,
				success:function(res){
				    console.log("ajax success")
                    window.location = "/"
				},
				error:function(res){
					console.log("error:"+res.code)
				}
			}).then(function(res){
				console.log("打印res.code:"+res.code);
				//登录验证的处理
			});
		}
	},
	
	//绑定事件函数
	bindEvents = function(selector){
		console.log("进入bindEvents")
		
		$(selector).find("[data-event]").each(function(){
			var $obj = $(this);
			var events = $(this).data("event").split(" ");
			var handler = $(this).data("handler").split(" ");
			//当一个节点上面的data-event和data-handler都不止1种时
			if( events.length>1 && handler.length>1 && events.length==handler.length ){
				$.each(events,function(i,v){
					$obj.off(events[i],EventHandler[handler[i]]).on(events[i],EventHandler[handler[i]]);
				})
			}
			//当event和handler都是一种时
			else{
				$obj.off($(this).data("event"),EventHandler[$(this).data("handler")]).on($(this).data("event"),EventHandler[$(this).data("handler")]);
			}
		})
	}
	
	bindEvents(".outer-wrap");
})
