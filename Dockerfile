FROM alpine:3.4

# install curl
RUN apk add --update curl bash 'go=1.6.2-r4' && rm -rf /var/cache/apk/*

# prepare go environment
ENV GOPATH /go
ENV GOROOT /usr/lib/go
ENV PATH $PATH:/usr/lib/go/bin:/go/bin

# add the current build context
ADD . /go/src/github.com/deis/helloworld

# compile the binary
RUN cd /go/src/github.com/deis/helloworld && go install -v .

EXPOSE 80

ENTRYPOINT ["/go/bin/helloworld"]
