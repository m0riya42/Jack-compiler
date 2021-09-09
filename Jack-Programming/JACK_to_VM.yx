import yoix.string.*;
import yoix.stdio.*;
import yoix.system.*;
import yoix.io.*;
import yoix.parser.*;
import yoix.string.*;
import yoix.*.*;
import yoix.util.*;

recognizeToken(tokStrFunc) //tokenizer
{
	int Ai,Ao;
	Array outArray, inArray, finalXY;
	String KeepYoixToXML;

	Dictionary tokens = {
		Array keyword ={"class", "constructor", "function", "method", "field", "static",
						"var", "int", "char", "boolean", "void", "true", "false", "null", "this", "let", "do",
						"if", "else", "while", "return"};
		Array symbol ={"{", "}","(",")","[","]",".",",",";","+","-","*","/","|","=","~"};//,"<",">","&"};
	};
		
	outArray = getDictionaryNames(tokens); //An array of names of all the arrays from the dictionary	

	for(Ao = 0; Ao<outArray@length; Ao++)
	{

		inArray=tokens[outArray[Ao]];
		for (Ai=0; Ai<inArray@length; Ai++)
		{	

			if (compareTo(tokStrFunc, inArray[Ai])==0)
			{						
				
				finalXY= new Array{outArray[Ao]," "+inArray[Ai]+" "};
				
				KeepYoixToXML= yoixToXML(finalXY); //Returns a string in the appropriate XML format
				return KeepYoixToXML+"\n";

			}
		}
	}
	//}
	
	return "-1"; //In case we have not yet finished reading the word
}

q0(jackLineArrQ0) //Q1 Q2 //tokenizer
{
	int q_0= this.index, flag=0;
	String recWordQ0="", recognizeTokenStrQ0;
	
	for(;q_0<jackLineArrQ0@length; q_0++)//Go through each character
	{
		if(regexec(this.recLetter, jackLineArrQ0[q_0]) && compareTo(jackLineArrQ0[q_0], " ")!=0)
		{
			recWordQ0+=jackLineArrQ0[q_0];
		}
		else break;
	} //When we got to a character that is not a letter we left
	
	if (q_0<jackLineArrQ0@length) //Just in case we did not finish reading the line
	{
		//Checks if the character is a letter, number, or underscore
		while  ((compareTo(jackLineArrQ0[q_0], "_")==0) || regexec(this.recNumber, jackLineArrQ0[q_0]) || regexec(this.recLetter, jackLineArrQ0[q_0]))
		{
			if (compareTo(jackLineArrQ0[q_0], " ")==0) //If we read a space we will get out of the loop
				break;
			flag=1; //Update the flag we got to ID
			recWordQ0+=jackLineArrQ0[q_0];
			
			//Promoting the index according to the conditions
			if (q_0<jackLineArrQ0@length-1)
				q_0++;
			else
			{	q_0++;
				break;
			}
		} 
	}
	if(flag==1)
		recognizeTokenStrQ0 = "<identifier> "+recWordQ0+" </identifier>\n";
	else recognizeTokenStrQ0 = recognizeToken(recWordQ0);
	if(compareTo(recognizeTokenStrQ0, "-1")==0) //Unreserved word
		 recognizeTokenStrQ0 = "<identifier> "+recWordQ0+" </identifier>\n";
	
	this.index = q_0;
	return recognizeTokenStrQ0;
}	

q3(jackLineArrQ3) //tokenizer
{
	int q_3= this.index;
	String recWordQ3="", recognizeTokenStrQ3;
	
	for(;q_3<jackLineArrQ3@length; q_3++)//Go through each character
	{
		if(regexec(this.recNumber, jackLineArrQ3[q_3]) && compareTo(jackLineArrQ3[q_3], " ")!=0)
		{
			recWordQ3+=jackLineArrQ3[q_3];
		}
		else break;
	}
	
	recognizeTokenStrQ3 = recognizeToken(recWordQ3);
	if(compareTo(recognizeTokenStrQ3, "-1")==0) //Unreserved word
		 recognizeTokenStrQ3 = "<integerConstant> "+recWordQ3+" </integerConstant>\n";
	
	this.index = q_3;
	return recognizeTokenStrQ3;
}	

q4(jackLineArrQ4) //tokenizer
{
	int q_4= this.index;
	String recWordQ4=jackLineArrQ4[q_4], recognizeTokenStrQ4;
	if (compareTo(recWordQ4, "<")==0)
	{
		recognizeTokenStrQ4 = "<symbol> &lt; </symbol>\n";

	}
	else if (compareTo(recWordQ4, ">")==0)
	{
		recognizeTokenStrQ4 = "<symbol> &gt; </symbol>\n";
	}
	else if (compareTo(recWordQ4, "&")==0)
	{
		recognizeTokenStrQ4 = "<symbol> &amp; </symbol>\n";
	}
	else {
		recognizeTokenStrQ4 = recognizeToken(recWordQ4);
		if(compareTo(recognizeTokenStrQ4, "-1")==0) //Unreserved word
			recognizeTokenStrQ4 = "Error: the tap  "+recWordQ4+"  not exist\n";
		}
	
	this.index = q_4+1;
	return recognizeTokenStrQ4;
}

q5(jackLineArrQ5) //tokenizer
{
	int q_5= this.index;
	String recWordQ5="" /*jackLineArrQ5[q_5]*/, recognizeTokenStrQ5;
	q_5++;
	for(;q_5<jackLineArrQ5@length; q_5++)//Go through each character
	{
		if(compareTo(jackLineArrQ5[q_5], "\"")!=0)
		{
			recWordQ5+=jackLineArrQ5[q_5];
		}
		else
		{
			q_5++;
			break;
		}
	}
	
	recognizeTokenStrQ5 = "<StringConstant> "+recWordQ5+" </StringConstant>\n";
	
	this.index = q_5;
	return recognizeTokenStrQ5;
}

q6(jackLineArrQ6) //Check if there is a comment //tokenizer
{
	int q_6= this.index;
	String recWordQ6=jackLineArrQ6[q_6], recognizeTokenStrQ6="";
	q_6++;
	this.noteFlag=1;
	
	if(q_6<jackLineArrQ6@length)
	{
	if(compareTo(jackLineArrQ6[q_6], "/")==0)
		{
			this.noteFlag=0;
			q_6 = jackLineArrQ6@length; //Read to the end of the line
		}
	else if (compareTo(jackLineArrQ6[q_6], "*")==0 && compareTo(jackLineArrQ6[q_6+1], "*")==0)
	{
		q_6 = q_6+2;
		for(;q_6<jackLineArrQ6@length; q_6++)//Go through each character
		{
			if(compareTo(jackLineArrQ6[q_6], "*")==0) //In case we found *
			{
				q_6++;
				if(compareTo(jackLineArrQ6[q_6], "/")==0) //A comment is over
				{
					q_6++;
					this.noteFlag=0;
					break; 
				}
				else this.noteFlag=1; //Go through the whole line and the comment is not over yet
			}
		}
	}
	else  {
	
		recognizeTokenStrQ6= recognizeToken(recWordQ6);
		this.noteFlag=0;
	}
	}
	this.index = q_6;
	return recognizeTokenStrQ6;
}

noteFunc(jackLineArrNote) //tokenizer
{
	int q_Note= this.index;
	String recWordNote="", recognizeTokenStrNote="";
	
	for(;q_Note<jackLineArrNote@length; q_Note++)//Go through each character
		{
			if(compareTo(jackLineArrNote[q_Note], "*")==0) //In case we found *
			{
				q_Note++;
				if (q_Note<jackLineArrNote@length)
				{
					if(compareTo(jackLineArrNote[q_Note], "/")==0) //A comment is over
					{
						q_Note++;
						this.noteFlag=0; //סיימנו את ההערה
						break; 
					}
				}
			}
		}
		
	
	this.index = q_Note;
	return recognizeTokenStrNote;
}

convertJackToXmlT(jackLine)  //Q0 //tokenizer
{
	String returnStr="", recognizeTokenStr, tokStr=""; 
	
	this.index=0;
	
	Array jackLineArr=strsplit(jackLine, ""); //Separates the string by the characters
	int t=0;
	
	while(t<jackLineArr@length)
	{
		tokStr=jackLineArr[t];
		if(this.noteFlag==1) //We're in the middle of a note
		{
			this.index=t;
			returnStr+= noteFunc(jackLineArr);
			t= this.index;
		}
		else if((compareTo(tokStr, " ")==0)||(compareTo(tokStr, "	")==0))
		{
			tokStr="";
			t++;
		}
		else if (compareTo(tokStr, "/")==0) 
		{
			this.index=t;
			returnStr+= q6(jackLineArr);
			t= this.index;
			
		}	
		else if (regexec(this.recLetter, tokStr)) //Starts with a letter
		{
			this.index=t;
			returnStr+= q0(jackLineArr);
			t= this.index;
		}
		else if (regexec(this.recNumber, tokStr))
		{
			this.index=t;
			returnStr+= q3(jackLineArr);
			t= this.index;
		}
		else if (regexec(this.recSymbol, toString(tokStr)) || (compareTo(tokStr, "]")==0) || (compareTo(tokStr, "[")==0))
		{
			
			this.index=t;
			returnStr+= q4(jackLineArr);
			t= this.index;
		}
		else if (compareTo(tokStr, "\"")==0)
		{
			this.index=t;
			returnStr+= q5(jackLineArr);
			t= this.index;
		}
		else
		{
			break;
		}
	}	
	return returnStr;
}

nextlineFunc() //parsing
{
	String nextlineFuncStr;
	if ((nextlineFuncStr = readLine(this.xmlTFile)) != NULL) //If we have not yet finished reading the file, there is another line /*xmlTFileP*/
	{
		this.xmlTLine = nextlineFuncStr;
		return true;
	}
	else {
		this.printCount=0;
		return false;
		}
}

findTheTokenName(xmlTLineFunc) //parsing
{
	
	Array xmlTLineArr; 
	xmlTLineArr=strsplit(xmlTLineFunc, " ");
		return xmlTLineArr[1]; //<X> tokenRead </X>
}

classVarDec() //ex5
{
	this.xmlFileP.nextline = "<classVarDec>";
		
	//ex5
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	this.kindH = this.tokenRead; // field / static
	if(compareTo(this.kindH, "field")==0)
	{
		this.indexHfield++;
		this.indexH= this.indexHfield;
	}
	else
	{	
		this.indexHstatic++;
		this.indexH= this.indexHstatic;
	}
	//ex5
	
	this.xmlFileP.nextline = this.xmlTLine; //<keyword> field / static </keyword>
	
	if(!nextlineFunc())
	{	this.endFileFlag=true;
		return;	} 
	this.xmlFileP.nextline = this.xmlTLine; //<keyword> type </keyword>
	
	//ex5
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	this.typeH = this.tokenRead; //type
	//ex5
	
	if(!nextlineFunc())
	{	this.endFileFlag=true;
		return;	} 
	this.xmlFileP.nextline = this.xmlTLine; //<identifier> varName </identifier>
	
	//ex5
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	this.nameH = this.tokenRead; //varName

	this.Class_scope.put(this.nameH, new Array{this.kindH, this.typeH,this.nameH, this.indexH});
	//ex5
			
	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag=true;
		return;	}  
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
			
	while(compareTo(this.tokenRead, ",")==0)
	{
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> , </symbol>
		if(!nextlineFunc())
		{	this.endFileFlag=true;
			return;	}
		this.xmlFileP.nextline = this.xmlTLine; //<identifier> varName </identifier>
		
		//ex5
		this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
		this.nameH = this.tokenRead; //varName
		
		if(compareTo(this.kindH, "field")==0)
		{
			this.indexHfield++;
			this.indexH= this.indexHfield;
		}
		else
		{	
			this.indexHstatic++;
			this.indexH= this.indexHstatic;
		}
		
		this.Class_scope.put(this.nameH, new Array{this.kindH, this.typeH,this.nameH, this.indexH});
		//ex5
		
		if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
		{	this.endFileFlag=true;
			return;	} 	
		this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	}
			
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> ; </symbol>
	
	this.xmlFileP.nextline = "</classVarDec>";
}
 
parameterList()  //ex5
{
	printf("parameterList() \n");
	this.xmlFileP.nextline = "<parameterList>";
	
	this.xmlFileP.nextline = this.xmlTLine; //this.tokenRead; //<identifier> void/ type </identifier> //<keyword>
	//ex5
	this.tokenRead= findTheTokenName(this.xmlTLine); //void/ type
	this.typeHM = this.tokenRead;
	this.kindHM = "argument";
	//ex5
	
	if(!nextlineFunc())
	{	this.endFileFlag=true;
		return;	} 
	this.xmlFileP.nextline = this.xmlTLine; //<identifier> varName </identifier>
	
	//ex5
	this.tokenRead= findTheTokenName(this.xmlTLine); //varName
	this.nameHM = this.tokenRead;
	this.indexHMA++;
	this.Method_scope.put(this.nameHM, new Array{this.kindHM, this.typeHM, this.nameHM, this.indexHMA})	;
	//ex5
	
	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag=true;
		return;	} 
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	
	printf("befor the while: %s\n", this.tokenRead);
	
	while(compareTo(this.tokenRead, ",")==0)
	{
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> , </symbol>
				
		if(!nextlineFunc())
		{	this.endFileFlag=true;
			return;	} 
		this.xmlFileP.nextline = this.xmlTLine;//this.tokenRead; //<identifier> void/ type </identifier> //<keyword>
		
		//ex5
		this.tokenRead= findTheTokenName(this.xmlTLine); //void/ type
		this.typeHM = this.tokenRead;
		this.kindHM = "argument";
		//ex5

		if(!nextlineFunc())
		{	this.endFileFlag=true;
			return;	} 
		this.xmlFileP.nextline = this.xmlTLine; //<identifier> varName </identifier>		

		//ex5
		this.tokenRead= findTheTokenName(this.xmlTLine); //varName
		this.nameHM = this.tokenRead;
		this.indexHMA++;
		this.Method_scope.put(this.nameHM, new Array{this.kindHM, this.typeHM, this.nameHM, this.indexHMA})	;
		//ex5

		if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
		{	this.endFileFlag=true;
			return;	}
		this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	}
	
	this.xmlFileP.nextline = "</parameterList>";
}

varDec()  //ex5
{
	this.xmlFileP.nextline = "<varDec>";
	
	this.xmlFileP.nextline = this.xmlTLine; //<keyword> var </keyword>
	
	if(!nextlineFunc())
	{	this.endFileFlag=true;
		return;	} 
	this.xmlFileP.nextline = this.xmlTLine; //<identifier> type </identifier> //<keyword>
	
	//ex5
	this.tokenRead= findTheTokenName(this.xmlTLine); //type
	this.typeHM = this.tokenRead;
	this.kindHM = "var";
	//ex5
	
	if(!nextlineFunc())
	{	this.endFileFlag=true;
		return;	} 
	this.xmlFileP.nextline = this.xmlTLine; //<identifier> varName </identifier> 
	
	//ex5
	this.tokenRead= findTheTokenName(this.xmlTLine); //varName
	this.nameHM = this.tokenRead;
	this.indexHMV++; 
	this.Method_scope.put(this.nameHM, new Array{this.kindHM, this.typeHM, this.nameHM, this.indexHMV})	;
	//ex5
	
	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag=true;
		return;	}  
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
			
	while(compareTo(this.tokenRead, ",")==0)
	{
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> , </symbol>
		
		if(!nextlineFunc())
		{	this.endFileFlag=true;
			return;	} 
		this.xmlFileP.nextline = this.xmlTLine; //<identifier> varName </identifier>
		
		//ex5
		this.tokenRead= findTheTokenName(this.xmlTLine); //varName
		this.nameHM = this.tokenRead;
		this.indexHMV++; 
		this.Method_scope.put(this.nameHM, new Array{this.kindHM, this.typeHM, this.nameHM, this.indexHMV})	;
		//ex5
		
		if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
		{	this.endFileFlag=true;
			return;	}
		this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	}
	
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> ; </symbol>
	
	this.xmlFileP.nextline = "</varDec>";
}

term() //ex5
{
	this.xmlFileP.nextline = "<term>";

	int termFlag=0;
	String tokX, strTemp_temp;
	
	if(this.expressionFlag==0) //if not, That means we have already moved on to the next line	
	{
		if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
		{	this.endFileFlag=true;
			return;	} 
	}
	else this.expressionFlag=0;
	 
	Array xmlTLineArrTerm; 
	xmlTLineArrTerm=strsplit(this.xmlTLine, " ");
	tokX= xmlTLineArrTerm[0]; //<tokX> ... </tokX>
	this.tokenRead = xmlTLineArrTerm[1]; //<X> tokenRead </X>
		
	//integerConstant
	if(compareTo(tokX,"<integerConstant>")==0)
	{
		this.xmlFileP.nextline = this.xmlTLine; //<integerConstant> num </integerConstant>
		//ex5
		this.tokenRead= findTheTokenName(this.xmlTLine); //num
		this.vmFile.nextline= "push constant "+ this.tokenRead; 	
		//ex5
	}
	//stringConstant
	else if(compareTo(tokX,"<StringConstant>")==0)
	{
		this.xmlFileP.nextline = this.xmlTLine; //<StringConstant> str </StringConstant>
		//ex5
		String strTempTerm;
		
		int sizeLine= this.xmlTLine@length-18;
		strTempTerm = substring(this.xmlTLine, 17 ,sizeLine);

		this.vmFile.nextline= "push constant "+ toString(strTempTerm@length); 
		this.vmFile.nextline= "call String.new 1";
		Array strTempTermArray = strsplit(strTempTerm, ""); //Separates the string by the characters
		int tempI;
		for(tempI=0; tempI< strTempTermArray@length; tempI++)
		{
			this.vmFile.nextline= "push constant "+toString(htob(atoh(strTempTermArray[tempI]))[0]);
			this.vmFile.nextline= "call String.appendChar 2";
		}
		//ex5
	}
	//keywordConstant
	else if (regexec(this.keywordConstant, this.tokenRead) && (compareTo(this.tokenRead, " ")!=0)) 
	{
		this.xmlFileP.nextline = this.xmlTLine; //<keywordConstant> true/ false/ null/ this </keywordConstant>
		if(compareTo(this.tokenRead, "true")==0)
			this.vmFile.nextline= "push constant 0\nnot\n";
		else if(compareTo(this.tokenRead, "false")==0)
			this.vmFile.nextline= "push constant 0";
		else if(compareTo(this.tokenRead, "null")==0)
			this.vmFile.nextline= "push constant 0";
		else if(compareTo(this.tokenRead, "this")==0)
			this.vmFile.nextline= "push pointer 0";
	}
	//varName //varName [ expression ]  //subroutineCall
	else if(compareTo(tokX,"<identifier>")==0)
	{
		strTemp_temp= this.tokenRead;
		if(compareTo(this.tokenRead, this.classNameP)==0) //subroutineCall
		{
			this.xmlFileP.nextline = this.xmlTLine; //<identifier> className </identifier>
			//ex5
			this.classNameSC= findTheTokenName(this.xmlTLine); //className
			this.classNameSCT = this.classNameSC;
			this.temp_SC= this.classNameSCT;
			//ex5
			
			if(!nextlineFunc())
			{	this.endFileFlag=true;
				return;	} 
			this.xmlFileP.nextline = this.xmlTLine; //<symbol> . </symbol>
			
			subroutineCallAfterTerm();
			if(this.endFileFlag==1) //If in the functions below the file is finished
				return;
		}
		else //varName / subroutineName
		{
			this.xmlFileP.nextline = this.xmlTLine; //<identifier> varName </identifier>
			
			//ex5
			this.varNameSC= findTheTokenName(this.xmlTLine); //varName
			this.classNameSCT = this.varNameSC;
			this.temp_SC= this.classNameSCT;
			//ex5
			
			if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
			{	this.endFileFlag=true;
				return;	} 
			this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
						
			if(compareTo(this.tokenRead, ".")==0) //subroutineCall
			{
				this.xmlFileP.nextline = this.xmlTLine; //<symbol> . </symbol>
				
				subroutineCallAfterTerm();
				if(this.endFileFlag==1) //If in the functions below the file is finished
					return;
			}
			else if(compareTo(this.tokenRead, "[")==0) 
			{
				this.xmlFileP.nextline = this.xmlTLine; //<symbol> [ </symbol>
				
				expression();
				if(this.endFileFlag==1) //If in the functions below the file is finished
					return;
				this.xmlFileP.nextline = this.xmlTLine; //<symbol> ] </symbol>
			
				//ex5
				Array varNameValuesTemp;
				String kindTemp; //, strTemp_temp= this.tokenRead;
				int flagVarTemp=0;
					if (Method_scope.contains(strTemp_temp)!=0 )
					{
						varNameValuesTemp = Method_scope.get(strTemp_temp);
					}
					else if (Class_scope.contains(strTemp_temp)!=0)
					{
						varNameValuesTemp = Class_scope.get(strTemp_temp);
					}
					
					kindTemp = varNameValuesTemp[0];
					
					if(compareTo(kindTemp, "var")==0)
						this.vmFile.nextline= "push local "+toString(varNameValuesTemp[3]);
					else if(compareTo(kindTemp, "argument")==0)
						this.vmFile.nextline= "push argument "+toString(varNameValuesTemp[3]);
					else if(compareTo(kindTemp, "field")==0)
						this.vmFile.nextline= "push this "+toString(varNameValuesTemp[3]);
					else if(compareTo(kindTemp, "static")==0)
						this.vmFile.nextline= "push static "+toString(varNameValuesTemp[3]);
				this.vmFile.nextline="add\npop pointer 1\npush that 0";

				//ex5
			}
			else if(compareTo(this.tokenRead, "(")==0) 
			{
				this.xmlFileP.nextline = this.xmlTLine; //<symbol> ( </symbol>
				
				if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
					{	this.endFileFlag=true;
						return;	} 		
				this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
								
				if(compareTo(this.tokenRead, ")")!=0)
				{
					this.expressionFlag=1; //##
					expressionList(); //expression();
					if(this.endFileFlag==1) //If in the functions below the file is finished
						return;
				}
				this.xmlFileP.nextline = this.xmlTLine; //<symbol> ) </symbol>
			}
			else  //varName
			{
				termFlag =1;
				
				//ex5
				Array varNameValuesTemp;
				String kindTemp; //, strTemp_temp= this.tokenRead;
				int flagVarTemp=0;
				

					if (Method_scope.contains(strTemp_temp)!=0 )
					{
						varNameValuesTemp = Method_scope.get(strTemp_temp);
					}
					else if (Class_scope.contains(strTemp_temp)!=0)
					{
						varNameValuesTemp = Class_scope.get(strTemp_temp);
					}
					else printf("the error !!! %s \n",strTemp_temp );
					
					kindTemp = varNameValuesTemp[0];
					
					if(compareTo(kindTemp, "var")==0)
						this.vmFile.nextline= "push local "+toString(varNameValuesTemp[3]);
					else if(compareTo(kindTemp, "argument")==0)
						this.vmFile.nextline= "push argument "+toString(varNameValuesTemp[3]);
					else if(compareTo(kindTemp, "field")==0)
						this.vmFile.nextline= "push this "+toString(varNameValuesTemp[3]);
					else if(compareTo(kindTemp, "static")==0)
						this.vmFile.nextline= "push static "+toString(varNameValuesTemp[3]);
				//ex5
			}
		}
		
	}	
	//( expression ) 
	else if(compareTo(this.tokenRead, "(")==0)
	{
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> ( </symbol>
		
		expression();
		if(this.endFileFlag==1) //If in the functions below the file is finished
			return;
		
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> ) </symbol>
	}
	// unaryOp term
	else if (regexec(this.unaryOp, this.tokenRead) && (compareTo(this.tokenRead, " ")!=0))
	{
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> -/~ </symbol>
		String termTemp= findTheTokenName(this.xmlTLine); // -/~

		term();
		if(this.endFileFlag==1) //If in the functions below the file is finished
			return;
		termFlag =1;
		
		if(compareTo(termTemp, "-")==0)
			this.vmFile.nextline="neg";
		else this.vmFile.nextline="not";

		
	}
	
	if (termFlag==0)
	{
		if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
			{	this.endFileFlag=true;
				return;	} 		
		this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	}
	
	this.xmlFileP.nextline = "</term>";
	//printf("Finish term() \n");
}

expression()  //ex5
{
	//printf("expression()\n");
	this.xmlFileP.nextline = "<expression>";
	
	String strExpression;
	
	
	term();
	if(this.endFileFlag==1) //If in the functions below the file is finished
		return;
	
	while(regexec(this.op, this.tokenRead) && (compareTo(this.tokenRead, " ")!=0)) //--> 0-*
	{
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> op </symbol>
		this.tokenRead= findTheTokenName(this.xmlTLine); //op
		strExpression=this.tokenRead;
		
		term();
		if(this.endFileFlag==1) //If in the functions below the file is finished
			return;
			
		
		//ex5
		if(compareTo(strExpression, "+")==0)
			this.vmFile.nextline="add";
		else if(compareTo(strExpression, "-")==0)
			this.vmFile.nextline="sub";
		else if(compareTo(strExpression, "*")==0)
			this.vmFile.nextline="call Math.multiply 2";
		else if(compareTo(strExpression, "/")==0)
			this.vmFile.nextline="call Math.divide 2";
		else if(compareTo(strExpression, "&amp;")==0)
			this.vmFile.nextline="and";
		else if(compareTo(strExpression, "|")==0)
			this.vmFile.nextline="or";
		else if(compareTo(strExpression, "&lt;")==0)
			this.vmFile.nextline="lt";
		else if(compareTo(strExpression, "&gt;")==0)
			this.vmFile.nextline="gt";
		else
		{
			this.vmFile.nextline="eq";
		}
		//ex5
	}
	
	this.xmlFileP.nextline = "</expression>";
}

expressionList() //ex5 
{
	this.xmlFileP.nextline = "<expressionList>";
	
	//ex5
	this.number_of_parameter=1;
	//ex5
	
	expression();
	if(this.endFileFlag==1) //If in the functions below the file is finished
		return;
	
	while(compareTo(this.tokenRead,",")==0)//-------->0-*
	{
		//ex5
		this.number_of_parameter++;
		//ex5
	
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> , </symbol>
		expression();
		if(this.endFileFlag==1) //If in the functions below the file is finished
			return;
	}
	
	this.xmlFileP.nextline = "</expressionList>";		
}

subroutineCallAfterTerm() //ex5
{
		
	if(!nextlineFunc())
	{	this.endFileFlag=true;
		return;	}
	this.xmlFileP.nextline = this.xmlTLine; //<identifier> subroutineName </identifier>
	//ex5
	String funcNameSC = findTheTokenName(this.xmlTLine); //subroutineName
	String classNameSCT2= this.classNameSCT;
	//ex5

	//ex5
		Array varNameValuesSC;
		String kindSC, typeSC;
		int flagVarSC=0;
		//varName
		if (Method_scope.contains(this.temp_SC)!=0 || Class_scope.contains(this.temp_SC)!=0) //(this.varNameSC)!=0
		{
			flagVarSC =1;
			if (Method_scope.contains(this.temp_SC)!=0 )
			{
				varNameValuesSC = Method_scope.get(this.temp_SC);
			}
			else if (Class_scope.contains(this.temp_SC)!=0)
			{
				varNameValuesSC = Class_scope.get(this.temp_SC);
			}
			
			kindSC = varNameValuesSC[0];
			typeSC= varNameValuesSC[1];
			if(compareTo(kindSC, "var")==0)
				this.vmFile.nextline= "push local "+toString(varNameValuesSC[3]);
			else if(compareTo(kindSC, "argument")==0)
				this.vmFile.nextline= "push argument "+toString(varNameValuesSC[3]);
			else if(compareTo(kindSC, "field")==0)
				this.vmFile.nextline= "push this "+toString(varNameValuesSC[3]);
			else if(compareTo(kindSC, "static")==0)
				this.vmFile.nextline= "push static "+toString(varNameValuesSC[3]);
		}
		//ex5

	if(!nextlineFunc())
	{	this.endFileFlag=true;
		return;	}
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> ( </symbol>
	
	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag=true;
		return;	} 
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	
	if (compareTo(this.tokenRead,")")!=0)
	{
		this.expressionFlag=1;
		expressionList();
		if(this.endFileFlag==1) //If in the functions below the file is finished
			return;
	}
	else this.xmlFileP.nextline = "<expressionList>\n</expressionList>";

	this.xmlFileP.nextline = this.xmlTLine; //<symbol> ) </symbol>
	
	if(flagVarSC==0)
	{
		this.vmFile.nextline= "call "+classNameSCT2+"."+funcNameSC+" "+toString(this.number_of_parameter);
		}
	else
		{ 
		this.vmFile.nextline= "call "+/*typeSC*/classNameSCT2+"."+funcNameSC+" "+toString(this.number_of_parameter);
		}

}

subroutineCall() //ex5
{
	this.number_of_parameter=0;

	//ex5
	String strTempSC;
	//ex5
	
	if(!nextlineFunc())	
	{	this.endFileFlag=true;
		return;	} 
	this.xmlFileP.nextline = this.xmlTLine; //<identifier> subroutineName/ className/ varName </identifier>
	
	//ex5
	this.tokenRead= findTheTokenName(this.xmlTLine); //subroutineName/ className/ varName
	strTempSC= this.tokenRead;
	//ex5
	
	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag=true;
		return;	} 
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	
	if(compareTo(this.tokenRead, "(")==0)
	{
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> ( </symbol>
		
		if(!nextlineFunc()) /*this.xmlTLine= nextlineFunc(); */
		{	this.endFileFlag=true;
			return;	}
		this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>

		//ex5
		this.vmFile.nextline= "push pointer 0";
		//ex5
		
		if(compareTo(this.tokenRead, ")")!=0)
		{
			this.expressionFlag=1; //##
			expressionList(); //expression();
			if(this.endFileFlag==1) //If in the functions below the file is finished
				return;
		}
		else this.xmlFileP.nextline = "<expressionList>\n</expressionList>";

		this.xmlFileP.nextline = this.xmlTLine; //<symbol> ) </symbol>
		
		//ex5
		this.vmFile.nextline= "call "+this.classNameP+"."+strTempSC+" "+toString(this.number_of_parameter+1);
		//ex5
		
	}
	else { // .
		
		//ex5
		Array varNameValuesSC;
		String kindSC, typeSC="typeSC";
		int flagVarSC=0;
		//varName
		if (Method_scope.contains(strTempSC)!=0 || Class_scope.contains(strTempSC)!=0)
		{
			flagVarSC =1;
			if (Method_scope.contains(strTempSC)!=0 )
			{
				varNameValuesSC = Method_scope.get(strTempSC);
			}
			else if (Class_scope.contains(strTempSC)!=0)
			{
				varNameValuesSC = Class_scope.get(strTempSC);
			}
			
			kindSC = varNameValuesSC[0];
			typeSC= varNameValuesSC[1];
			if(compareTo(kindSC, "var")==0)
				this.vmFile.nextline= "push local "+toString(varNameValuesSC[3]);
			else if(compareTo(kindSC, "argument")==0)
				this.vmFile.nextline= "push argument "+toString(varNameValuesSC[3]);
			else if(compareTo(kindSC, "field")==0)
				this.vmFile.nextline= "push this "+toString(varNameValuesSC[3]);
			else if(compareTo(kindSC, "static")==0)
				this.vmFile.nextline= "push static "+toString(varNameValuesSC[3]);
		}
		//ex5
		
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> . </symbol>
		
		if(!nextlineFunc()) 
		{	this.endFileFlag=true;
			return;	}
		this.xmlFileP.nextline = this.xmlTLine; //<identifier> subroutineName </identifier>
		
		//ex5
		String funcNameSC= findTheTokenName(this.xmlTLine); //subroutineName
		//ex5
		
		if(!nextlineFunc())
		{	this.endFileFlag=true;
			return;	}
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> ( </symbol>
				
		if(!nextlineFunc()) /*this.xmlTLine= nextlineFunc(); */
		{	this.endFileFlag=true;
			return;	}
		this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	
		if(compareTo(this.tokenRead, ")")!=0)
		{
			this.expressionFlag=1; //for the term func
			expressionList(); //expression();
			if(this.endFileFlag==1) //If in the functions below the file is finished
				return;
		}
		else this.xmlFileP.nextline = "<expressionList>\n</expressionList>";

		this.xmlFileP.nextline = this.xmlTLine; //<symbol> ) </symbol>
		
		//ex5
		if(flagVarSC==1)
		{
			if(compareTo(this.classNameP, "Main")==0)
				this.vmFile.nextline= "call "+typeSC+"."+funcNameSC/*strTempSC*/+" "+toString(this.number_of_parameter+1); 
			else this.vmFile.nextline= "call "+strTempSC/*typeSC*/+"."+funcNameSC/*strTempSC*/+" "+toString(this.number_of_parameter+1); 
		}
		else this.vmFile.nextline= "call "+strTempSC+"."+funcNameSC+" "+toString(this.number_of_parameter);
		
		//ex5
	}
	
	this.number_of_parameter=0;
}
 
letStatement()  //ex5
{
	//printf("letStatement() \n");
	this.xmlFileP.nextline = "<letStatement>";
	
	//ex5
	String varNameLS;
	int flagLS=0;
	//ex5
	
	this.xmlFileP.nextline = this.xmlTLine; //<keyword> let </keyword>
	
	if(!nextlineFunc())
	{	this.endFileFlag=true;
		return;	}
	this.xmlFileP.nextline = this.xmlTLine; //<identifier> varName </identifier>
	
	//ex5
	this.tokenRead= findTheTokenName(this.xmlTLine); //varName
	varNameLS= this.tokenRead;
	//ex5
	
	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag=true;
		return;	} 
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	
	//ex5
	Array varNameValuesLT;
	String kindLS;
	if (Method_scope.contains(varNameLS)!=0)
		{
			varNameValuesLT = Method_scope.get(varNameLS);
		}
	else if (Class_scope.contains(varNameLS)!=0)
		{
			varNameValuesLT = Class_scope.get(varNameLS);
		}
	else 	printf("varNameLS: %s\n", varNameLS);

	kindLS = varNameValuesLT[0];
	//ex5
	
	
	if (compareTo(this.tokenRead,"[")==0) 	//--->0-1
	{
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> [ </symbol>
		
		expression();
		if(this.endFileFlag==1) //If in the functions below the file is finished
			return;
		
		//ex5
		flagLS =1; //We are with an array
		
		if(compareTo(kindLS, "var")==0)
			this.vmFile.nextline= "push local "+toString(varNameValuesLT[3]);
		else if(compareTo(kindLS, "argument")==0)
			this.vmFile.nextline= "push argument "+toString(varNameValuesLT[3]);
		else if(compareTo(kindLS, "field")==0)
			this.vmFile.nextline= "push this "+toString(varNameValuesLT[3]);
		else if(compareTo(kindLS, "static")==0)
			this.vmFile.nextline= "push static "+toString(varNameValuesLT[3]);
		
		this.vmFile.nextline= "add";

		//ex5
		
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> ] </symbol> 
		
		if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
		{	this.endFileFlag=true;
			return;	}
		this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	}
	
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> = </symbol>
	
	expression();
	if(this.endFileFlag==1) //If in the functions below the file is finished
		return;

	if(flagLS==1) //We are with an array
	{
		this.vmFile.nextline= "pop temp 0\npop pointer 1\npush temp 0\npop that 0";
		flagLS=0;
	}
	else
	{
		if(compareTo(kindLS, "var")==0)
			this.vmFile.nextline= "pop local "+toString(varNameValuesLT[3]);
		else if(compareTo(kindLS, "argument")==0)
			this.vmFile.nextline= "pop argument "+toString(varNameValuesLT[3]);
		else if(compareTo(kindLS, "field")==0)
			this.vmFile.nextline= "pop this "+toString(varNameValuesLT[3]);
		else if(compareTo(kindLS, "static")==0)
			this.vmFile.nextline= "pop static "+toString(varNameValuesLT[3]);
	}
	
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> ; </symbol>

	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag=true;
		return;	} 
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	
	this.xmlFileP.nextline = "</letStatement>";
}

ifStatement() //ex5
{
	this.xmlFileP.nextline = "<ifStatement>";
	
	this.xmlFileP.nextline = this.xmlTLine; //<keyword> if </keyword>
	
	if(!nextlineFunc())
	{	this.endFileFlag=true;
		return;	}
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> ( </symbol>
	
	expression();
	if(this.endFileFlag==1) //If in the functions below the file is finished
		return;
	
	//ex5
	int indexIFS= this.indexLIF++;
	
	this.vmFile.nextline= "if-goto IF_TRUE"+toString(indexIFS);
	this.vmFile.nextline= "goto IF_FALSE"+toString(indexIFS);
	this.vmFile.nextline= "label IF_TRUE"+toString(indexIFS);	
	//ex5
	
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> ) </symbol>
	
	if(!nextlineFunc())
	{	this.endFileFlag=true;
		return;	}
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> { </symbol>
	
	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag=true;
		return;	} 
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	
	statements();
	if(this.endFileFlag==1) //If in the functions below the file is finished
		return;
		
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> } </symbol>
	
	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag=true;
		return;	} 
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	
	if (compareTo(this.tokenRead,"else")==0) 	//--->0-1
	{
		//ex5
		this.vmFile.nextline= "goto IF_END"+toString(indexIFS);
		this.vmFile.nextline= "label IF_FALSE"+toString(indexIFS);
		//ex5
	
		this.xmlFileP.nextline = this.xmlTLine; //<keyword> else </keyword> 
		
		if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
		{	this.endFileFlag=true;
			return;	}
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> { </symbol>
		
		if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */   //##
		{	this.endFileFlag=true;
			return;	} 
		this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
		
		statements();
		if(this.endFileFlag==1) //If in the functions below the file is finished
			return;
			
		//ex5
		this.vmFile.nextline= "label IF_END"+toString(indexIFS);
		//ex5
		
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> } </symbol> 
		
		if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
		{	this.endFileFlag=true;
			return;	}
		this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	}
	else 
	{	
		//ex5
		this.vmFile.nextline= "label IF_FALSE"+toString(indexIFS); 
		//ex5
	}
	
	this.xmlFileP.nextline = "</ifStatement>";
}

whileStatement() //ex5
{
	printf("whileStatement() \n");
	this.xmlFileP.nextline = "<whileStatement>";

	this.xmlFileP.nextline = this.xmlTLine; //<keyword> while </keyword>
	
	//ex5
	int indexWhile= this.indexLWhile++;
	this.vmFile.nextline = "label WHILE_EXP"+toString(indexWhile); 
	//ex5
	
	if(!nextlineFunc())
	{	this.endFileFlag=true;
		return;	}
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> ( </symbol>
	
	expression();
	if(this.endFileFlag==1) //If in the functions below the file is finished
		return;

	//ex5
	this.vmFile.nextline = "not\n if-goto WHILE_END"+toString(indexWhile); 
	//ex5
	
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> ) </symbol>
	
	if(!nextlineFunc())
	{	this.endFileFlag=true;
		return;	}
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> { </symbol>
	
	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag=true;
		return;	}
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	
	statements();
	
	//ex5
	this.vmFile.nextline = "goto WHILE_EXP"+toString(indexWhile);
	this.vmFile.nextline = "label WHILE_END"+toString(indexWhile); 	
	//ex5
		
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> } </symbol>
	
	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag=true;
		return;	}
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	
	this.xmlFileP.nextline = "</whileStatement>";
	printf("Finish whileStatement() \n");
}

doStatement() 
{
	this.xmlFileP.nextline = "<doStatement>";
	
	this.xmlFileP.nextline = this.xmlTLine; //<keyword> do </keyword>
	
	subroutineCall();
	if(this.endFileFlag==1) //If in the functions below the file is finished
		return;
	
	if(!nextlineFunc())	
	{	this.endFileFlag=true;
		return;	}
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> ; </symbol>
	
	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag=true;
		return;	} 
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
		
	this.xmlFileP.nextline = "</doStatement>";
}

returnStatement()  //ex5
{
	this.xmlFileP.nextline = "<returnStatement>";
	
	this.xmlFileP.nextline = this.xmlTLine; //<keyword> return </keyword>
	
	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
		{	this.endFileFlag=true;
			return;	} 	
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	
	
	
	if (compareTo(this.tokenRead,";")!=0) 	//--->0-1
	{
		this.expressionFlag=1;//Because we're already promoted a line
		expression();
		if(this.endFileFlag==1) //If in the functions below the file is finished
				return;
	}
	//ex5
	else this.vmFile.nextline= "push constant 0";
	//ex5
	
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> ; </symbol>
	
	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
		{	this.endFileFlag=true;
			return;	} 	
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>	
	
	this.xmlFileP.nextline = "</returnStatement>";
	
	//ex5
	this.vmFile.nextline="return";
	//ex5
}

statement() //ex5
{
	//printf("statement() \n");
	
	while(compareTo(this.tokenRead, "}")!=0)
	{
		if(compareTo(this.tokenRead, "let")==0)
		{
			letStatement();
			if(this.endFileFlag==1) //If in the functions below the file is finished
				return;
		}
		else if(compareTo(this.tokenRead, "if")==0)
		{
			ifStatement();
			if(this.endFileFlag==1) //If in the functions below the file is finished
				return;
		}
		else if(compareTo(this.tokenRead, "while")==0)
		{
			whileStatement();
			if(this.endFileFlag==1) //If in the functions below the file is finished
				return;
			
		}
		else if(compareTo(this.tokenRead, "do")==0)
		{
			doStatement();
			if(this.endFileFlag==1) //If in the functions below the file is finished
				return;
			//ex5
			this.vmFile.nextline="pop temp 0";
			//ex5
			

		}
		else if(compareTo(this.tokenRead, "return")==0)
		{
			returnStatement();
			if(this.endFileFlag==1) //If in the functions below the file is finished
				return;
		}
		this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>		
	}
}

statements() 
{
	this.xmlFileP.nextline = "<statements>";
	
	statement();//0-*
	if(this.endFileFlag==1) //If in the functions below the file is finished
		return;
	
	this.xmlFileP.nextline = "</statements>";
}

subroutineBody()  //ex5
{
	this.xmlFileP.nextline = "<subroutineBody>";
	
	this.xmlFileP.nextline = this.xmlTLine;//this.tokenRead; //<symbol> { </symbol>
	
	//varDec()---->0-*
	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag=true;
		return;	} 
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	
	while(compareTo(this.tokenRead, "var")==0)
	{
		varDec();
		if(this.endFileFlag==1) //If in the functions below the file is finished
				return;
	
		if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
		{	this.endFileFlag=true;
			return;	} 
		this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	
	}
	
	//ex5
	Array keysM2= this.Method_scope.keys;
	int SD, numOfParameter, counterSD=0;
	Array SDarray;
	for (SD=0; SD< keysM2@length; SD++)
	{
		SDarray = this.Method_scope.values[SD];
		if(compareTo(SDarray[0],"var")==0)
			counterSD++;
	}
	this.vmFile.nextline = "function "+ this.classNameP+"."+this.subroutineNameP+" "+toString(counterSD); 
	
	Array subroutineBodyArray, SBAraay;
	int SB, varCount=0;
	if(compareTo(this.funcType, "constructor")==0)
	{
		subroutineBodyArray= this.Class_scope.keys;
		for(SB=0; SB<subroutineBodyArray@length; SB++)
		{
			SBAraay= this.Class_scope.values[SB];
			if(compareTo(SBAraay[0], "field")==0)
				varCount++;
		}
		this.vmFile.nextline= "push constant "+  toString(varCount);
		this.vmFile.nextline= "call Memory.alloc 1";
		this.vmFile.nextline= "pop pointer 0"; // = 'this'

	}
	else if(compareTo(this.funcType, "method")==0)
	{
		this.vmFile.nextline= "push argument 0";
		this.vmFile.nextline= "pop pointer 0";       //= RAM[THIS]  
	}
	//ex5
	
	statements(); //Once
	if(this.endFileFlag==1) //If in the functions below the file is finished
			return;
	
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> } </symbol>	
	
	this.xmlFileP.nextline = "</subroutineBody>";

}

subroutineDec()  //ex5
{
	this.xmlFileP.nextline = "<subroutineDec>";
	
	//ex5
	int HM=0;
	Array keysM;
	
	keysM= Method_scope.keys;
	if(keysM@length>0){
		for (HM=0; HM<keysM@length; HM++)
		{
			Method_scope.remove(keysM[HM]);  //Reset the icon table before handling a new file
		} 
	}
	indexHMA=-1; indexHMV=-1;
	//ex5
	
	this.xmlFileP.nextline = this.xmlTLine; //<keyword> constructor/ method/ function </keyword>
		
	//ex5
	this.tokenRead= findTheTokenName(this.xmlTLine); // constructor/ method/ function 
	this.funcType= this.tokenRead;
	if(compareTo(this.funcType, "method")==0)
	{
		indexHMA++;
		this.Method_scope.put("this", new Array{"argument", this.classNameP, "this", indexHMA});
	}
	//ex5
	
	if(!nextlineFunc())
	{	this.endFileFlag==1;
		return;	} 
	this.xmlFileP.nextline = this.xmlTLine; //<identifier> void/ type </identifier> //<keyword>
	
	if(!nextlineFunc())
	{	this.endFileFlag==1;
		return;	}
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X> 
	this.subroutineNameP = this.tokenRead; 
	this.xmlFileP.nextline = this.xmlTLine; //<identifier> subroutineName </identifier> 
	
	if(!nextlineFunc())
	{	this.endFileFlag==1;
		return;	}
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> ( </symbol>

	if(!nextlineFunc()) /*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag==1;
		return;	} 
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	
	printf("befor parameterList: %s\n", this.tokenRead);
	
	//parameterList() ---->0-1
	if(compareTo(this.tokenRead, this.classNameP)==0 || compareTo(this.tokenRead, "int")==0 || compareTo(this.tokenRead, "char")==0 || compareTo(this.tokenRead, "boolean")==0 || compareTo(this.tokenRead, "Array")==0)
	{
			
		parameterList();

		if(this.endFileFlag==1) //If in the functions below the file is finished
		{
			return;
		}
		
	}
	else this.xmlFileP.nextline = "<parameterList>\n</parameterList>";

	
	this.xmlFileP.nextline = this.xmlTLine; //<symbol> ) </symbol>
	
	if(!nextlineFunc()) /*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag==1;
		return;	} 
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
	
	subroutineBody();
	if(this.endFileFlag==1) //If in the functions below the file is finished
				return;
	
	this.xmlFileP.nextline = "</subroutineDec>";
}

convertXmlTtoXML() 
{
	if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
	{	this.endFileFlag==1;
		return; } 
	this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
			
	if(compareTo(this.tokenRead, "class")==0)
	{
		this.xmlFileP.nextline = "<class>";
		this.xmlFileP.nextline = this.xmlTLine; //<keyword> class </keyword>
		
		if(!nextlineFunc()) 					
		{	this.endFileFlag==1;
			return;	} 
		this.xmlFileP.nextline = this.xmlTLine; //<identifier> className </identifier>
		
		this.tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
		this.classNameP= this.tokenRead;

		
		if(!nextlineFunc()) 					
		{	this.endFileFlag==1;
			return;	} 
		this.xmlFileP.nextline = this.xmlTLine; //<symbol> { </symbol>
	
		if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
		{	this.endFileFlag==1;
			return;	} 
		tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>
		
		//classVarDec();---->0-*
		while(compareTo(this.tokenRead, "static")==0 || compareTo(this.tokenRead, "field")==0)
		{
			classVarDec();	
			if(this.endFileFlag==1) //If in the functions below the file is finished
				return;
				
			if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
			{	this.endFileFlag==1;
				return;	} 
			tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>			
		}

		//subroutineDec();---->0-*
		while(compareTo(this.tokenRead, "constructor")==0 || compareTo(this.tokenRead, "method")==0 || compareTo(this.tokenRead, "function")==0)
		{
			subroutineDec();
			if(this.endFileFlag==1) //If in the functions below the file is finished
				return;
			
			if(!nextlineFunc())	/*this.xmlTLine= nextlineFunc(); */
			{	this.endFileFlag==1;
				return;	} 			
			tokenRead= findTheTokenName(this.xmlTLine); //<X> tokenRead </X>	
		}
		
		xmlFileP.nextline = this.xmlTLine; //<symbol> } </symbol>
		this.xmlFileP.nextline = "</class>";
		
	}
}

//Main

Hashtable Class_scope, Method_scope;
String nameH, typeH, kindH, nameHM, typeHM, kindHM, vmFileName, funcType, classNameSC, varNameSC, classNameSCT, temp_SC;
int indexH=-1, indexHstatic=-1, indexHfield=-1,h, indexHMA=-1, indexHMV=-1, indexLIF=0, indexLWhile=0;
int number_of_parameter= 0, flagWhile=0;
Array keys;
File vmFile;


//Global variables
Regexp recLetter, recNumber, recSymbol, recQuet;
recLetter.pattern = "[a-z | A-Z]";
recNumber.pattern = "[0-9]"; 
recSymbol.pattern = "[-|{ | }|(|)|.|,|;|+|*|/|=|~|<|>|&]";  
int index=0, noteFlag=0, expressionFlag=0;

int endFileFlag=0, printCount=0;
String classNameP, subroutineNameP, tokenRead, xmlTLine; 
Regexp op, unaryOp, keywordConstant ;
op.pattern = "[-|+|*|/|=|<|>|&|]"; 
unaryOp.pattern="[-|~]"; 
keywordConstant.pattern = "(true)|(false)|(null)|(this)";
File xmlFileP;

String pathS, str, xmlFileName, line, pathStr, lineXML="";
int i, j;
Array files, array, arrayFileNameASM, folderName, filesP, arrayP;
File jackFile, xmlTFile; //To a file named from it

pathS="C:\\Users\\moriy\\Desktop\\ex5";
printf("Start\n"); 

while (isDirectoryPath(pathS)!=1)//Loop until the input is correct
{
	printf("Enter libarry's path!\n"); 
	pathS = stdin.nextline;
}

files = directoryListing(pathS);//The input of the library name 

//tokenizer

printf("start tokenizer\n");  

for(i=0; i<files@length; i++)
{
	array = strsplit(files[i], "."); //Divides by points
	if(compareTo(array[array@length-1],"jack")==0) //If the suffixis JACK
	{
		str = files[i];
		if ((jackFile = fopen(str, "r")) != NULL) { //If we were able to open the file
			
			//We will need to create a new file with the same name and translate there
			xmlFileName = array[array@length-2] + "T.xml";
			File xmlFileTokenizer = fopen(""+pathS+"\\"+xmlFileName , "w");
			
			xmlFileTokenizer.nextline = "<tokens>";
			
			while ((line = readLine(jackFile)) != NULL){ //If we have not yet finished reading the file, there is another line
				
				if(line@length!=0)
				{
				if (line@length > 1)
				{
					if (compareTo(substring(line, 0 ,2), "//")!=0) //Check that this is not a comment
					{	lineXML = convertJackToXmlT(line);
						if(compareTo(lineXML,"")!=0)
							xmlFileTokenizer.nextline =  substring(lineXML, 0 ,lineXML@length-1); } //Lowers the last /n
				}
				else {
						lineXML = convertJackToXmlT(line);
						if(compareTo(lineXML,"")!=0)
							xmlFileTokenizer.nextline =  substring(lineXML, 0 ,lineXML@length-1); 
				}
				}

			 }
			 
			xmlFileTokenizer.nextline = "</tokens>";

			//Close the files
			fclose(xmlFileTokenizer);
			fclose(jackFile); 
		}

		//If we were not able to open the file
		else printf("Error with openning the file: %s\n",str); 
		
	}
}

printf("Finish tokenizer\n"); 

//parser

printf("start Parsing\n");

filesP = directoryListing(pathS);//The input of the library name 
String parsingFileName, parsingFileNameSuffix, strP="";

for(i=0; i<filesP@length; i++)
{
	strP = filesP[i]; //keeps the name of the file
	arrayP = strsplit(filesP[i], "."); //Divides by points

	parsingFileName = arrayP[arrayP@length-2];
	parsingFileNameSuffix= substring(parsingFileName, parsingFileName@length-1 ,parsingFileName@length); // the last char of the file name
	
	if((compareTo(arrayP[arrayP@length-1],"xml")==0) && (compareTo(parsingFileNameSuffix,"T")==0)) //if the file is XML and the last char of the file is T
	{
		if ((xmlTFile = fopen(strP, "r")) != NULL) { //If we were able to open the file
			
			//We will need to create a new file with the same name and translate there
			xmlFileName =  substring(arrayP[arrayP@length-2], 0 ,arrayP[arrayP@length-2]@length-1) + ".xml";
			//ex5
			vmFileName = substring(arrayP[arrayP@length-2], 0 ,arrayP[arrayP@length-2]@length-1) + ".vm";
			//ex5
			
			xmlFileP = fopen(""+pathS+"\\"+xmlFileName , "w");
			//ex5
			vmFile = fopen(""+pathS+"\\"+vmFileName , "w");
			//ex5
			
			nextlineFunc(); // -<tokens> נדלג על 
			printf("\n\nStart the files: %s, %s \n\n",xmlFileName, vmFileName ); 
			
			indexLIF=0;
			indexLWhile=0;
			convertXmlTtoXML(); 
			
			keys = Class_scope.keys;
			
			for (h=0; h<keys@length; h++)
				Class_scope.remove(keys[h]);  //Reset the icon table before handling a new file
			indexHstatic=-1; indexHfield=-1; indexH=-1;
				
			//ex5
			
			printf("\n\nFinish the file: %s  \n\n",xmlFileName ); 
			endFileFlag=0;
				
			//Close the files
			fclose(xmlFileP);
			fclose(xmlTFile); 
		}
			 
		
			//If we were not able to open the file
		else printf("Can not read from the file: %s\n",strP); 
	}
}
		
printf("Finish Parsing\n");
