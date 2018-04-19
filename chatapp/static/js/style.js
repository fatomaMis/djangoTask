function func(){
    var input=document.getElementById("message_input").value;
    var email=document.getElementById("email").value;

    if(email == ''){
        alert("you have to enter email")
    }
    else{
    var ul=document.getElementById("message");  
    $.post("/chatapp/home/send",
    {
      data: input,
      emaildata:email,
    },
    function(data,status){
        var li=document.createElement("LI");
        li.innerHTML=input;
        ul.appendChild(li);
        document.getElementById("message_input").value=" ";
        document.getElementById("email").value=" ";
    });
}
}
