var num = document.getElementsByTagName('input').text;
var neg = true;
var total = 1;
function leibniz(){
  for (var i = 3; i < num; i+2){
    if (neg) {
      total -= 1/i;
    }
    else {
      total += 1/i;
    }
    neg = !neg;
  }
  document.getElementsByTagName('p').text = total * 4;
}
