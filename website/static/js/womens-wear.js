var ul = document.getElementById("ul_pr");
var li = document.querySelectorAll("li");
//var all_in= document.querySelectorAll("input").value;


function add(id){
    // var del_new = document.createElement("button");
    var li_new = document.createElement("li");
    var li_inp = document.createTextNode(id);
    
    //hidden input 
    //var input= document.createElement("input");
    //input.value= id
    //alert(all_in)
    //input.style.display="none"
    //alert(input.value)
    //ul.appendChild(input);

    li_new.appendChild(li_inp);
    // li_new.appendChild(document.createTextNode( '\u00A0\u00A0' ) );
    ul.appendChild(li_new);
    // var del_inp = document.createTextNode("Del");
    // del_new.appendChild(del_inp);
    // li_new.appendChild(del_new);
    ul.appendChild(document.createElement("br"));
}

function copyText(){
  var text= document.getElementById("ul_pr");
  var next= text.children;
  let list=[];
  for(let i=0; i< next.length; i++){
   word=next[i].innerHTML;
   words= word+ " ".replace(/,/g, ' ');
    list.push(words);
  }
  if ((list.length) < 1){
    alert("List is empty! ")
  } 
  else{
    list.concat(" ");
    //document.body.append(list);
    navigator.clipboard.writeText(list);
    alert("text copied")
  }

}

/*function copy(){
  let div= document.getElementById("div");
  let text= div.innerText;
  let textArea= document.createElement("textarea");
  textArea.width= "1px";
  textArea.height= "1px";
  textArea.background= "transparent";
  textArea.value= text;
  document.body.append(textArea);
  textArea.select();
  document.execCommand("copy");
  document.body.removeChild(textArea);


}*/





window.emptyList = function () {
    var ul = document.querySelector('#ul_pr');
    var listLength = ul.children.length;
  
    for (i = 0; i < listLength; i++) {
      ul.removeChild(ul.children[0]);
    }
  }