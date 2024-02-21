CC=clang
CFLAGS=  -fopenmp=libomp
LDFLAGS= -fopenmp

libddm.so: ddm.o
	$(CC)  ddm.o -dynamiclib -o libddm.so $(LDFLAGS)
	$(MAKE) clean

ddm.o: ddm.c
	$(CC) $(CFLAGS) -c ddm.c

clean:
	rm *.o

