$(document).ready(function(){
    $("#field").next().css("background-color","#F00000");
});
$(":checkbox").click(function() {
    if ($(this).is(":checked")){
        if($(this).closest("tr").prev().attr("id") == "field" || $(this).closest("tr").prev().css("color") == 'rgb(204, 204, 204)'){
            // チェック状態であれば、取り消し線と背景、文字色を変更
            $(this).closest("tr").css("text-decoration", "line-through");
            $(this).closest("tr").css("color","#CCCCCC");
            console.log($(this).closest("tr").next().css("color"))

            if($(this).closest("tr").next().css("color") != 'rgb(204, 204, 204)'){
                $(this).closest("tr").next().css("background-color","#F00000");
            }
        }

        // チェック状態で背景色が赤色であれば白色に変更
        if($(this).closest("tr").css("background-color") == "rgb(240, 0, 0)"){
            $(this).closest("tr").css("background-color","#FFFFFF");
        }
        
    }
    else {
        if(($(this).closest("tr").prev().attr("id") == "field" || $(this).closest("tr").prev().css("color") == 'rgb(204, 204, 204)') && $(this).closest("tr").next().css("color") != 'rgb(204, 204, 204)'){
            // 非チェック状態であれば、取り消し線の除去、背景、文字色を変更
            $(this).closest("tr").css("text-decoration", "none");
            $(this).closest("tr").css("background-color","#FFFFFF");
            $(this).closest("tr").css("color","#000000");
            $(this).closest("tr").next().css("background-color","#FFFFFF");

            // 非チェックにしたとき、前の要素に強調色を付ける
            if($(this).closest("tr").prev().css("background-color") != 'rgb(240, 0, 0)'){
                $(this).closest("tr").css("background-color","#F00000");
            }
        }

    }
});