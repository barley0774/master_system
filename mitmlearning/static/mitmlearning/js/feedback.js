function show_info(num, id){
    console.log(id)
    if (num == 0){
        document.getElementById(id).style.display="block";
    }else{
        document.getElementById(id).style.display="none";
    }
}

// show_info 継承
function show_credentials(num, id){
    show_info(num, id);
    let table = document.getElementById('credentials');
    var row = table.rows.length;
    if (row > 1 && $('#credentials').is(':visible')){
        document.body.style.backgroundColor = "#F6AA00";
    }else{
        document.body.style.backgroundColor = "#fff";
    }
}