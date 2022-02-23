<h1> spider_js</h1>
<i> A Spider with Javascript using Splash</i>


The following project is a challenge requested by [Zyte](https://www.zyte.com/) </br>
This project has been developed on Windows 

<h2>Installation</h2>

Click on Code and then on Download Zip.</br>
Or create a folder, open git bash and run:
<pre><code> git clone https://github.com/LucasDamianR/spider_js.git </code></pre>

In order for it to work you must install requirements.txt. 

• cd to the directory where requirements.txt is located</br>
• activate your virtualenv (recommended)</br>
run in your shell:
<pre><code>pip install -r requirements.txt</code></pre>

<h3> Docker for Windows with wsl2</h3>

• [installation guide](https://docs.docker.com/desktop/windows/wsl/)

<h3> Scrapy Splash </h3>

• [installation guide](https://github.com/scrapy-plugins/scrapy-splash)

<h2>Running the project</h2>

Make sure you have the container running on port 8050 and in <code>settings.py</code></br>
run in terminal:
<pre><code>scrapy crawl quote -o quote.json</code></pre>
