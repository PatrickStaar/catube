function play_media(title,data,type,description) {
    var area=document.getElementById('media-area');
    var shut=document.getElementById('media-shut');
    var shadow=document.getElementById('shadow');
    var desc=document.getElementById('media-desc');
    var attach=''
    area.style.display='block';
    shadow.style.display='block';
    desc.style.display='block';
    if(type == 'img'){
    attach='<img class="media-content" align="middle" src="'+data+'">'
    }
    else{
    attach='<video class="media-content" controls style="padding:0px"><source src="'+data+'" type="video/mp4"></video>'
    }
    area.innerHTML=attach;
    desc.innerHTML= '<h3 style="color:white;">'+description+'</h3>';
    }

function close_window() {
    var area=document.getElementById('media-area');
    var shut=document.getElementById('media-shut');
    var shadow=document.getElementById('shadow');
    var desc=document.getElementById('media-desc');
    area.style.display='none';
    shadow.style.display='none';
    desc.style.display='none';
}
function search(){
    var word=document.getElementById("search").value;
    if(word != ""){
        window.open("http://127.0.0.1:8000/search?keyword="+word);
    }
}
function check(){
    var pass1=document.getElementsByName("new-pass")[0].value;
    var pass2=document.getElementsByName("confirm-pass")[0].value;
    if(pass1!=pass2){
              alert("密码不一致");
         }
}

