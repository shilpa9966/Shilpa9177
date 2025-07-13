function add()
{
var num1,num2,sum;
num1=parseInt(document.getElementById("txtFirstNumber").value);
num2=parseInt(document.getElementById("txtSecondNumber").value);
sum=num1+num2;
document.getElementById("txtAnswer").value=sum;
}
function sub()
{
var num1,num2,sub;
num1=parseInt(document.getElementById("txtFirstNumber").value);
num2=parseInt(document.getElementById("txtSecondNumber").value);
sub=num1-num2;
document.getElementById("txtAnswer").value=sub;
}
function abc()
{
var num1,num2,abc;
num1=parseInt(document.getElementById("txtFirstNumber").value=" 0" );
num2=parseInt(document.getElementById("txtSecondNumber").value=" " );
abc=num1+num2;
document.getElementById("txtAnswer").value=" ";
}