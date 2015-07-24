/*
 * css样式中含有form-valid
 * －－－－－－－－－－－－
 * 控件属性：
 * －－－－－－－－－－－－
 * valid-func 验证方法，验证控件值是否有效
 * valid-event 验证事件，可触发验证的控件事件
 * valid-required 是否强制验证，在验证表单时，是否要求验证
 * valid-warn-func 显示验证提示信息方法
 * 
 * －－－－－－－－－－－－
 * 控件方法
 * －－－－－－－－－－－－
 * bindValidEvent 绑定验证事件，可动态绑定控件的验证事件
 * validForm 验证表单，验证表单中输入框
 * 
 * 实例：
 * <input type="password" class="form-control form-valid" 
 * name="passwordConfirm" 
 * id="tvPasswordConfirm" placeholder="确认密码" 
 * warn-control="divWarnPwdConfirm" 
 * valid-func="check_passwordconfirm" 
 * valid-event="blur" 
 * valid-required="true" 
 * valid-warn-func='warn_passwordconfirm'>
 * */
	$(document).bind("ready",function(){
		$(".form-valid").bindValidEvent();
	});
	
	$.fn.extend({
		showMessage:function(message,level){
			var func=eval($(this).attr("valid-warn-func"));
			func(level,true,message);
		},
		hideMessage:function(level){
			var func=eval($(this).attr("valid-warn-func"));
			func(level,false,"");
		},
		bindValidEvent:function(){
			var o=$(this);
			
			$(this).each(function(n,i){
				var event=$(i).attr("valid-event");
				var func=$(i).attr("valid-func");
				i.valid=eval(func);
				$(i).bind(event,i.valid);
			});
		},
		
		validForm:function(){
			var valided=true;
			$(this).find(".form-valid").each(function(n,i){
					var required=$(i).attr("valid-required");
					if(required=="true"){
						if(!i.valid()){
							valided=false;
						}
					}
				});
			
			return valided;
		}
	});