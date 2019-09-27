document.getElementById("answersData").style.display = "none";
document.getElementById("display-1").style.display = "none";
document.getElementById("display-2").style.display = "none";
document.getElementById("display-3").style.display = "none";
document.getElementById("display-4").style.display = "none";
document.getElementById("button-1").style.display = "none";
document.getElementById("size-of-corpus").style.display = "none";
document.getElementById("algorithm").style.display = "none";
document.getElementById("feature").style.display = "none";
document.getElementById("print-answer").style.display = "none";

function selectLanguage()
{
	document.getElementById("display-1").style.display = "block";
	document.getElementById("size-of-corpus").style.display = "block";
}

function selectSizeOfCorpus() 
{
	document.getElementById("display-2").style.display = "block";
	document.getElementById("algorithm").style.display = "block";	
}

function selectAlgorithm() 
{
	document.getElementById("display-3").style.display = "block";
	document.getElementById("feature").style.display = "block";	
}

function selectFeature() 
{
	document.getElementById("display-4").style.display = "block";
	document.getElementById("button-1").style.display = "block";	
}

function checkAccuracy() 
{
	answers = document.getElementById('answersData').innerHTML;
	answers = answers.substr(1).slice(0, -1);
	answers = answers.substr(1);
	answers = JSON.parse(answers);
	
	ff = document.getElementById("language").value;
	ss = document.getElementById("size-of-corpus").value;
	tt = document.getElementById("algorithm").value;
	ffo = document.getElementById("feature").value;
	
	if(answers[ff][ss][tt][ffo]!=undefined)
	{
		document.getElementById("print-answer").innerHTML="<br/>" + "Accuracy is : " + answers[ff][ss][tt][ffo];
		document.getElementById("print-answer").style.display = "block";	
	}
	
	else
	{
		document.getElementById("print-answer").style.display = "none";	
	}
}