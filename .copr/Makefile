srpm:
	dnf -y install rpmdevtools
	rpmbuild -D "_srcrpmdir $(outdir)" -D "_sourcedir $(spec:D:h)/.." -bs $(spec)