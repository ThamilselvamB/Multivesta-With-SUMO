

// ----------- running multivesta implementation ------------------//
javac -cp ~/sumo/bin/multivesta.jar multivestaTesting.java



// ------------- running sumo part -----------------------------//




javac -cp ~/sumo/bin/libsumo-1.8.0-SNAPSHOT.jar socket1.java

java -Djava.library.path=.  -cp libsumo-1.8.0-SNAPSHOT.jar:. socket1















// aditional infor..............//

bash$ export CLASSPATH="path/to/jar/file:path/tojar/file2"
bash$ javac MyMainClass.java




// How to execute this program .................................................

javac -cp libsumo-1.8.0-SNAPSHOT.jar:multivesta.jar:. sumoState.java 
java -Djava.library.path=. -cp libsumo-1.8.0-SNAPSHOT.jar:multivesta.jar:. sumoState


java -Djava.library.path=. -cp multivesta.jar:libsumo-1.8.0-SNAPSHOT.jar:. vesta.mc.NewVestaServer 49141

java -Djava.library.path=. -cp libsumo-1.8.0-SNAPSHOT.jar:multivesta.jar:. vesta.NewVesta -sd sumoState -m data/cross.sumocfg -f quatex/expr1.quatex -l serversLists/oneLocalServer -vp TRUE -bs 30 -a 0.1 -d1 2.0 -sots 0 -osws	 WHOLESIMULATION
