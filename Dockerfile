FROM python:3.6.2-jessie

# Discord
RUN pip install discord.py==0.16.8

# Julia
ENV JULIA_PATH /usr/local/julia
ENV JULIA_VERSION 0.6.0

RUN mkdir $JULIA_PATH \
	&& curl -sSL "https://julialang-s3.julialang.org/bin/linux/x64/${JULIA_VERSION%[.-]*}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz" -o julia.tar.gz \
	&& tar -xzf julia.tar.gz -C $JULIA_PATH --strip-components 1 \
	&& rm julia.tar.gz*

ENV PATH $JULIA_PATH/bin:$PATH
ADD . /app
WORKDIR /app

CMD python app.py
