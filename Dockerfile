FROM python:3.5

ADD . /app
WORKDIR /app

RUN pip install -U discord.py

ENV JULIA_PATH /usr/local/julia
ENV JULIA_VERSION 0.6.0

RUN mkdir $JULIA_PATH

RUN curl -sSL "https://julialang-s3.julialang.org/bin/linux/x64/${JULIA_VERSION%[.-]*}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz" -o julia.tar.gz

RUN tar -xzf julia.tar.gz -C $JULIA_PATH --strip-components 1
RUN rm -rf /var/lib/apt/lists/* julia.tar.gz*
#julia-903644385b
ENV PATH $JULIA_PATH/bin:$PATH

CMD python app.py