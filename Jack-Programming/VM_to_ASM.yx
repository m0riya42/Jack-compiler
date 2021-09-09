import yoix.string.*;
import yoix.stdio.*;
import yoix.system.*;
import yoix.io.*;

countX=1;

pushFunc(pushVmLineArray, nameClass1)
{
	String strDefine;
	int intTemp;
	if (pushVmLineArray@length > 2) //Avoid exception  if we approach a place in an array that does not exist
	{	
			if (compareTo(pushVmLineArray[1], "temp")==0) //push temp NUM
			{	
				intTemp=5;
				for( i=0; i<atoi(pushVmLineArray[2]); i++)
					intTemp++;
				return "@"+toString(intTemp)+"\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1";
			}
			else if (compareTo(pushVmLineArray[1], "static")==0) //push static NUM
			{
				return "@"+nameClass1+"."+pushVmLineArray[2]+"\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1";
			}
			else if (compareTo(pushVmLineArray[1], "pointer")==0) //push pointer NUM (0\1)
			{
				if (compareTo(pushVmLineArray[2], "0")==0) //push pointer 0
					strDefine="THIS";
				else if (compareTo(pushVmLineArray[2], "1")==0) //push pointer 1
					strDefine="THAT";
				return "@" + strDefine + "\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1";
			}
			else if (compareTo(pushVmLineArray[1], "constant")==0) //push constant NUM
			{
				return "@"+pushVmLineArray[2]+"\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1";
			}
			else{	//local,that, argument, this,
			if (compareTo(pushVmLineArray[1], "local")==0) //push local NUM
				strDefine="LCL";
			else if (compareTo(pushVmLineArray[1], "argument")==0) //pop argument NUM
				strDefine="ARG";
			else if (compareTo(pushVmLineArray[1], "this")==0) //pop this NUM
				strDefine="THIS";
			else if (compareTo(pushVmLineArray[1], "that")==0) //pop that NUM
				strDefine="THAT";
			else
				printf("problem in the input: "+ popVmLineArray[1]); 		
		
			return "@" + pushVmLineArray[2] + "\nD=A\n@"+strDefine+"\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1";
		}
			
	}	
}

addFunc()
{
	return "@SP\nA=M-1\nD=M\nA=A-1\nM=D+M\n@SP\nM=M-1";
}

subFunc()
{
	return "@SP\nA=M-1\nD=M\nA=A-1\nM=M-D\n@SP\nM=M-1";
}

popFunc(popVmLineArray, nameClass)
{
	String strTemp="", strDefine;
	int i, intTemp;
	if (popVmLineArray@length > 2)
	{
		
		if (compareTo(popVmLineArray[1], "temp")==0) //pop temp NUM
			{	
				intTemp=5;
				for( i=0; i<atoi(popVmLineArray[2]); i++)
					intTemp++;
				return "@SP\nA=M-1\nD=M\n@" + toString(intTemp) + "\nM=D\n@SP\nM=M-1";
			}
		
		else if (compareTo(popVmLineArray[1], "static")==0)//pop static NUM
		{
			return "@SP\nA=M-1\nD=M\n@"+ nameClass+"." + popVmLineArray[2] + "\nM=D\n@SP\nM=M-1";
		}
		
		else if (compareTo(popVmLineArray[1], "pointer")==0)//pop pointer NUM (0/1)
		{
			if (compareTo(popVmLineArray[2], "0")==0) //pop pointer 0
				strDefine="THIS";
			else if (compareTo(popVmLineArray[2], "1")==0) //pop pointer 1
				strDefine="THAT";
			return "@SP\nA=M-1\nD=M\n@" + strDefine + "\nM=D\n@SP\nM=M-1";
		}
		
		else{	//local, argument, this, that
		if (compareTo(popVmLineArray[1], "local")==0) //pop local NUM
			strDefine="LCL";
		else if (compareTo(popVmLineArray[1], "argument")==0) //pop argument NUM
			strDefine="ARG";
		else if (compareTo(popVmLineArray[1], "this")==0) //pop this NUM
			strDefine="THIS";
		else if (compareTo(popVmLineArray[1], "that")==0) //pop that NUM
			strDefine="THAT";
		else
			printf("problem in the input: "+ popVmLineArray[1]); 		
		
		for(i=0; i<atoi(popVmLineArray[2]); i++)//Adds this line several times according to the number we got
			strTemp+="A=A+1\n";					//atoi - Converts from string to number
		return "@SP\nA=M-1\nD=M\n@"+strDefine+"\nA=M\n" + strTemp + "M=D\n@SP\nM=M-1";		
		}		
	}			
}

eqFunc()
{
	return "@SP\nA=M-1\nD=M\nA=A-1\nD=D-M\n@IF_TRUE0\nD;JEQ\nD=0\n@SP\nA=M-1\nA=A-1\nM=D\n@FINALEQ\n0;JMP\n(IF_TRUE0)\nD=-1\n@SP\nA=M-1\nA=A-1\nM=D\n(FINALEQ)\n@SP\nM=M-1";
}

ltFunc() //In case it is correct returns -1 otherwise returns 0
{
	return "@SP\nA=M-1\nD=M\nA=A-1\nD=D-M\n@IF_TRUE1\nD;JGT\nD=0\n@SP\nA=M-1\nA=A-1\nM=D\n@FINALLT\n0;JMP\n(IF_TRUE1)\nD=-1\n@SP\nA=M-1\nA=A-1\nM=D\n(FINALLT)\n@SP\nM=M-1";
}

gtFunc() //In case it is correct returns -1 otherwise returns 0
{
	return "@SP\nA=M-1\nD=M\nA=A-1\nD=D-M\n@IF_TRUE2\nD;JLT\nD=0\n@SP\nA=M-1\nA=A-1\nM=D\n@FINALGL\n0;JMP\n(IF_TRUE2)\nD=-1\n@SP\nA=M-1\nA=A-1\nM=D\n(FINALGL)\n@SP\nM=M-1";
}

negFunc() 
{
	return "@SP\nA=M-1\nD=M\nM=-D";
}

notFunc() 
{
	return "@SP\nA=M-1\nM=!M";
}

orFunc()
{
	return "@SP\nM=M-1\n@SP\nA=M\nD=M\n@SP\nM=M-1\n@SP\nA=M\nA=M\nD=D|A\n@SP\nA=M\nM=D\n@SP\nM=M+1";
}

andFunc()
{
	return "@SP\nM=M-1\n@SP\nA=M\nD=M\n@SP\nM=M-1\n@SP\nA=M\nA=M\nD=D&A\n@SP\nA=M\nM=D\n@SP\nM=M+1";
}

labelFunc(labelVmLineArray,labelNameClass)
{
	return "("+ labelNameClass +"." +labelVmLineArray[1]+")";
}

gotoFunc(gotoVmLineArray,gotoNameClass)
{
	return "@"+gotoNameClass+"."+gotoVmLineArray[1]+"\n0; JMP";
}

ifGotoFunc(ifGotoVmLineArray,ifGotoNameClass)
{
	return "@SP\nM=M-1\nA=M\nD=M\n@"+ifGotoNameClass+"."+ifGotoVmLineArray[1]+"\nD; JNE";

}

functionFunc(functionVmLineArray)
{
		return "(" + functionVmLineArray[1] + ")\n@"+ functionVmLineArray[2] + "\nD=A\n@"+ functionVmLineArray[1] +".End\nD; JEQ\n("+ functionVmLineArray[1] +".Loop)\n@SP\nA=M\nM=0\n@SP\nM=M+1\n@"+ functionVmLineArray[1] +".Loop\nD=D-1;JNE \n("+ functionVmLineArray[1] +".End)";
}

returnFunc()
{
	return "@LCL\nD=M\n@5\nA=D-A\nD=M\n@13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@ARG\nA=M\nM=D\n@ARG\nD=M\n@SP\nM=D+1\n@LCL\nM=M-1\nA=M\nD=M\n@THAT\nM=D\n@LCL\nM=M-1\nA=M\nD=M\n@THIS\nM=D\n@LCL\nM=M-1\nA=M\nD=M\n@ARG\nM=D\n@LCL\nM=M-1\nA=M\nD=M\n@LCL\nM=D\n@13\nA=M\n0; JMP";
}	

callFunc(callVmLineArray, callNameClass,countCallFunc)
{
	// push return-address
	String returnStr = "@"+callNameClass+"."+callVmLineArray[1]+countCallFunc+"\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n";
	// push LCL
	returnStr += "@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n";
	// push ARG
	returnStr += "@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n";
	// push THIS
	returnStr += "@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n";
	// push THAT
	returnStr += "@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n";
	// ARG = SP-n-5 
	intTemp=5;
	for( i=0; i<atoi(callVmLineArray[2]); i++)
		intTemp++;
	returnStr += "@SP\nD=M\n@" + toString(intTemp) + "\nD=D-A\n@ARG\nM=D\n";
	// LCL = SP
	returnStr += "@SP\nD=M\n@LCL\nM=D\n";
	// goto g
	returnStr += "@"+ callVmLineArray[1]+"\n0; JMP\n";
	//label return-address
	returnStr += "("+ callNameClass+"."+ callVmLineArray[1] + countCallFunc +")";
	return returnStr;
	
}


convertVmToAsm(vmLine, nameClass){
	
		Array vmLineArray = strsplit(vmLine, " "); //Divides the string by the space and puts each word in the array
		String asmLine= "";
		if (compareTo(vmLineArray[0], "push")==0)
			asmLine+= pushFunc(vmLineArray,nameClass );
		else if (compareTo(vmLineArray[0], "add")==0)
			asmLine+= addFunc();
		else if (compareTo(vmLineArray[0], "sub")==0)
			asmLine+= subFunc();
		else if (compareTo(vmLineArray[0], "pop")==0)
			asmLine+= popFunc(vmLineArray, nameClass);
		else if (compareTo(vmLineArray[0], "eq")==0)
			asmLine+= eqFunc();
		else if (compareTo(vmLineArray[0], "lt")==0)
			asmLine+= ltFunc();
		else if (compareTo(vmLineArray[0], "gt")==0)
			asmLine+= gtFunc();
		else if (compareTo(vmLineArray[0], "neg")==0)
			asmLine+= negFunc();
		else if (compareTo(vmLineArray[0], "not")==0)
			asmLine+= notFunc();
		else if (compareTo(vmLineArray[0], "or")==0)
			asmLine+= orFunc();
		else if (compareTo(vmLineArray[0], "and")==0)
			asmLine+= andFunc();
		else if (compareTo(vmLineArray[0], "label")==0)
			asmLine+= labelFunc(vmLineArray,nameClass);
		else if (compareTo(vmLineArray[0], "goto")==0)
			asmLine+= gotoFunc(vmLineArray,nameClass);
		else if (compareTo(vmLineArray[0], "if-goto")==0)
			asmLine+= ifGotoFunc(vmLineArray,nameClass);
		else if (compareTo(vmLineArray[0], "function")==0)
			asmLine+= functionFunc(vmLineArray);
		else if (compareTo(vmLineArray[0], "return")==0)
			asmLine+= returnFunc();
		else if (compareTo(vmLineArray[0], "call")==0)
		{
			
			asmLine+= callFunc(vmLineArray, nameClass, toString(this.countCall) );
			this.countCall++;
		}
		else asmLine+="YOU FORGOT THE "+vmLineArray[0]+" FUNC!!!!!!";
		return asmLine;
}




//Main

String pathS, str, asmFileName, line, pathStr;
int i, j, countCall=1;
Array files, array, arrayFileNameASM, folderName;
File vmFile; //to the file that we will read from it


printf("Please enter libarry's path: \n"); 
pathS = stdin.nextline;
printf("Start\n");


while (isDirectoryPath(pathS)!=1)//Loop until the input is correct
{
	printf("Enter libarry's path!\n");
	pathS = stdin.nextline;
}
files = directoryListing(pathS);//The input of the library name
Array  vmFileArray[files@length];//Array of VM files in a folder
int countVM=0;

for(i=0; i<files@length; i++) //Check how many VM files we have and save their names in the array
{
	array = strsplit(files[i], "."); //Divides by points
	if(compareTo(array[array@length-1],"vm")==0) //If the suffix is VM

	{
		vmFileArray[countVM] = files[i];
		countVM++;
	}
}

if (countVM == 1)
{
	str = vmFileArray[0]; //File name being read
	pathStr=pathS+"\\"+str; //We will connect the file name with the folder in which the file is read
	if ((vmFile = fopen(pathStr, "r")) != NULL) { //If we were able to open the file
			arrayFileNameASM = strsplit(vmFileArray[0], "."); //Divides by points
			//נצטרך ליצור קובץ חדש עם אותו שם ונתרגם שם
			asmFileName = arrayFileNameASM[0] + ".asm";
			File asmFile = fopen(""+pathS+"\\"+asmFileName , "w");
						
			 while ((line = readLine(vmFile)) != NULL){ //If we have not yet finished reading the file, there is another line
				if (line@length > 1)
					if (compareTo(substring(line, 0 ,2), "//")!=0) //Check that this is not a comment
						asmFile.nextline = convertVmToAsm(line, array[array@length-2]); //Call the function and writing the returned value in the new file
			}
			
			//Close the files
			fclose(asmFile);
			fclose(vmFile); 
		}
	else printf("Error with openning the file");
}

else if (countVM > 1)//In case there is more than one VM file
{

	folderName = strsplit(pathS, "\\"); //Divides by points	
	asmFileName = folderName[folderName@length-1] + ".asm";
	File asmFile = fopen(""+pathS+"\\"+asmFileName , "w");
			
	for(j=0; j<countVM; j++)
	{
		arrayFileNameASM = strsplit(vmFileArray[j], "."); //Divides by points

		if (compareTo(arrayFileNameASM[0],"Sys")==0) //We want this file to open first
		{
			str = vmFileArray[j]; //The name of the file who called
			pathStr=pathS+"\\"+str; //We will connect the file name with the folder in which the file is read
			if ((vmFile = fopen(pathStr, "r")) != NULL) { //If we were able to open the file
				
			asmFile.nextline="@256\nD=A\n@SP\nM=D";
			asmFile.nextline= convertVmToAsm("call Sys.init 0", arrayFileNameASM[0]); 
			 while ((line = readLine(vmFile)) != NULL){ //If we have not yet finished reading the file, there is another line
				if (line@length > 1)
					if (compareTo(substring(line, 0 ,2), "//")!=0) //Check that this is not a comment
						asmFile.nextline = convertVmToAsm(line, arrayFileNameASM[0]); //Call the function and writing the returned value in the new file
				}
			fclose(vmFile); 
			}
			else printf("Error with openning the file");
		}
	}
	for(i=0; i<countVM; i++)
	{
		arrayFileNameASM = strsplit(vmFileArray[i], "."); //Divides by points

		if (compareTo(arrayFileNameASM[0],"Sys")!=0) //We will open the rest of the files and add their translation to a file we have already opened
		{
			str = vmFileArray[i]; //The name of the file called
			pathStr=pathS+"\\"+str; //We will connect the file name with the folder in which the file is read
			
			if ((vmFile = fopen(pathStr, "r")) != NULL) { //If we were able to open the file
				while ((line = readLine(vmFile)) != NULL){ //If we have not yet finished reading the file, there is another line
					if (line@length > 1)
						if (compareTo(substring(line, 0 ,2), "//")!=0) //Check that this is not a comment
							asmFile.nextline = convertVmToAsm(line, arrayFileNameASM[0]); //Call the function and writing the returned value in the new file
				}
			
			fclose(vmFile); 
			}
			else printf("Error with openning the file");

		}
	}	
	fclose(asmFile);
}


