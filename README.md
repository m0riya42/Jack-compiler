# Jack-Compiler using Yoix
## Compiler to Jack language using Yoix Scripting Language.

(NAND-to-Tetris---add )
The Yoix interpreter is built using 100% pure JavaTM technology and its language includes the
best bits and many familiar constructs from both Java and C plus a few twists of its own.
(<cite>'An Introduction to the YoixTM Interpreter'</cite> by Richard Drechsler and John Mocenigo)


### Preparing the Workspace
* Install java workspace- [jdk-download](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html)
* Add path to the system's paths- [set-path-explanation ](https://www.computerhope.com/issues/ch000549.htm)
* Download and Extract Yoix- [download-yoix](https://github.com/att/yoix)

### Run "Hello World" in Yoix
* Enter the extracted folder with the 'yoix.jar' file
* Create new file called 'hello_world.yx'
* Enter the file and write: 
```md
import yoix.*.*;
printf("hello world\n"); 
```
<pre>
** in order to run the file, open commandLine from the folder and write: <b> java  -jar  yoix.jar  hello_world.yx </b> 
** in order to prevent memory problems add '-Xmx512m' to the line above. 
(resizing memory location to 512m instead of 64m (default))
</pre>

https://github.com/att/yoix

https://www.nand2tetris.org/

The Jack Compiler can be used to compile Jack source code into a virtual machine language. (For use with the Nand2Tetris module: https://www.nand2tetris.org/)

Build instructions
Compile each Java class individually javac <javaclass> or all with javac *.java.

Usage
Run the compiler on a file or directory java com.JackCompiler <file/directory name>

  
