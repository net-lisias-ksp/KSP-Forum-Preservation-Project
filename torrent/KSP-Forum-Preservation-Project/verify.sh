#!/usr/bin/env bash

verify() {
	ssh-keygen -Y verify -f ./allowed_signers -I net.lisias.ksp-Forum-Preservation-Project -n $1.sig -s $1.sig < $1
}


verify allowed_signers
for f in *.lrz ;  do
	verify $f
done
