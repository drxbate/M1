$(document).bind("ready",function(){
	$(".selector[control-role]").each(funciton(i,e){
		if(e.tagName!="input"){
			return true;
		}
		
	});
});