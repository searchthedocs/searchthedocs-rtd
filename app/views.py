# -*- coding: utf-8 -*-
from functools import wraps
import json

from flask import render_template

from app import app

@app.route('/')
@app.route('/section')
def index():
    context = {
        'JS_VERSION': app.config['JS_VERSION'],
        'PROD_JS': app.config['PROD_JS'],
    }
    return render_template('index.html', **context)

@app.route('/projects/search/autocomplete/')
def mock_domain_list_api():
    return json.dumps({
        'results': ["abalt-django.ajax", "Django Appregister", "Asas Django",
                    "django-ccfiletypes", "cookiecutter-django-cms",
                    "djacap - DJango ACcounting APplication", "Django",
                    "Django-1.4-zh_cn-tkliuxing", "Django Absolute",
                    "Django-achievements", "django-achtung", "django-activeurl",
                    "django-activity-stream", "django adaptors",
                    "django-ad-code", "Django Addendum", "django-admin2",
                    "django-adminactions", "django-admin-extensions",
                    "django-admin-honeypot", "datapusher", "disco"]
    })

@app.route('/api/v2/search/section/')
def mock_sections_api():
    return json.dumps({
        "results": {
            "hits": {
                "hits": [
                    {
                        "_type": "section",
                        "_index": "readthedocs-20131026230446",
                        "_score": 396.33047,
                        "fields": {
                            "project": "docs",
                            "title": "Custom install Documentation",
                            "content": "\n<h2>Custom install Documentation<a class=\"headerlink\" href=\"#custom-install-documentation\" title=\"Permalink to this headline\">\u00b6</a></h2>\n<div class=\"toctree-wrapper compound\">\n<ul>\n<li class=\"toctree-l1\"><a class=\"reference internal\" href=\"custom_installs/\">Info about custom installs</a><ul>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"custom_installs/customization/\">Customizing your install</a><ul>\n<li class=\"toctree-l3\"><a class=\"reference internal\" href=\"custom_installs/customization/#have-a-local-settings-file\">Have a local settings file</a></li>\n<li class=\"toctree-l3\"><a class=\"reference internal\" href=\"custom_installs/customization/#adding-your-own-title-to-pages\">Adding your own title to pages</a></li>\n</ul>\n</li>\n</ul>\n</li>\n</ul>\n</div>\n",
                            "version": "latest",
                            "path": "index",
                            "page_id": "custom-install-documentation"
                        },
                        "highlight": {
                            "content": [
                                "\n<h2>Custom <em>install</em> Documentation<a class=\"headerlink\" href=\"#custom-<em>install</em>-documentation\" title",
                                " your <em>install</em></a><ul>\n<li class=\"toctree-l3\"><a class=\"reference internal\" href=\"custom_installs"
                            ],
                            "title": [
                                "Custom <em>install</em> Documentation"
                            ]
                        },
                        "_id": "38bc2be6c92ab096ed94e49d1eae0fe9"
                    },
                    {
                        "_type": "section",
                        "_index": "readthedocs-20131026230446",
                        "_score": 10.6348,
                        "fields": {
                            "project": "docs",
                            "title": "USE_PIP_INSTALL",
                            "content": "\n<h2>USE_PIP_INSTALL<a class=\"headerlink\" href=\"#use-pip-install\" title=\"Permalink to this headline\">\u00b6</a></h2>\n<p>Default: <a class=\"reference external\" href=\"http://python.readthedocs.org/en/latest/library/constants.html#False\" title=\"(in Python v3.4)\"><tt class=\"xref py py-obj docutils literal\"><span class=\"pre\">False</span></tt></a></p>\n<p>Whether to use <tt class=\"xref py py-obj docutils literal\"><span class=\"pre\">pip</span> <span class=\"pre\">install</span> <span class=\"pre\">.</span></tt> or <tt class=\"xref py py-obj docutils literal\"><span class=\"pre\">python</span> <span class=\"pre\">setup.py</span> <span class=\"pre\">install</span></tt> when installing packages into the Virtualenv. Default is to use <tt class=\"xref py py-obj docutils literal\"><span class=\"pre\">python</span> <span class=\"pre\">setup.py</span> <span class=\"pre\">install</span></tt>.</p>\n",
                            "version": "latest",
                            "path": "settings",
                            "page_id": "use-pip-install"
                        },
                        "highlight": {
                            "content": [
                                "\n<h2>USE_PIP_<em>INSTALL</em><a class=\"headerlink\" href=\"#use-pip-<em>install</em>\" title=\"Permalink to this headline",
                                " literal\"><span class=\"pre\">pip</span> <span class=\"pre\"><em>install</em></span> <span class=\"pre\">.</span></tt",
                                "\">setup.py</span> <span class=\"pre\"><em>install</em></span></tt> when installing packages into the Virtualenv",
                                " class=\"pre\">setup.py</span> <span class=\"pre\"><em>install</em></span></tt>.</p>\n"
                            ],
                            "title": [
                                "USE_PIP_<em>INSTALL</em>"
                            ]
                        },
                        "_id": "a5485e66d40c8d594f5c9f97d54460a5"
                    },
                    {
                        "_type": "section",
                        "_index": "readthedocs-20131026230446",
                        "_score": 0.5345826,
                        "fields": {
                            "project": "docs",
                            "title": "Developer Documentation",
                            "content": "\n<h2>Developer Documentation<a class=\"headerlink\" href=\"#developer-documentation\" title=\"Permalink to this headline\">\u00b6</a></h2>\n<div class=\"toctree-wrapper compound\">\n<ul>\n<li class=\"toctree-l1\"><a class=\"reference internal\" href=\"install/\">Installation</a><ul>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"install/#solr-search-setup\">Solr (Search) Setup</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"install/#what-s-available\">What\u2019s available</a></li>\n</ul>\n</li>\n<li class=\"toctree-l1\"><a class=\"reference internal\" href=\"todo/\">Todo</a><ul>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"todo/#easy\">Easy</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"todo/#sprintable\">Sprintable</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"todo/#design\">Design</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"todo/#hard-refactors\">Hard/Refactors</a></li>\n</ul>\n</li>\n<li class=\"toctree-l1\"><a class=\"reference internal\" href=\"contribute/\">Contributing to Read the Docs</a><ul>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"contribute/#translations\">Translations</a></li>\n</ul>\n</li>\n<li class=\"toctree-l1\"><a class=\"reference internal\" href=\"architecture/\">Architecture</a><ul>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"architecture/#diagram\">Diagram</a></li>\n</ul>\n</li>\n<li class=\"toctree-l1\"><a class=\"reference internal\" href=\"settings/\">Interesting Settings</a><ul>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"settings/#use-subdomain\">USE_SUBDOMAIN</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"settings/#production-domain\">PRODUCTION_DOMAIN</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"settings/#varnish-servers\">VARNISH_SERVERS</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"settings/#multiple-app-servers\">MULTIPLE_APP_SERVERS</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"settings/#slumber-username\">SLUMBER_USERNAME</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"settings/#slumber-password\">SLUMBER_PASSWORD</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"settings/#index-only-latest\">INDEX_ONLY_LATEST</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"settings/#document-pyquery-path\">DOCUMENT_PYQUERY_PATH</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"settings/#use-pip-install\">USE_PIP_INSTALL</a></li>\n</ul>\n</li>\n<li class=\"toctree-l1\"><a class=\"reference internal\" href=\"tests/\">Running tests</a><ul>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"tests/#continuous-integration\">Continuous Integration</a></li>\n</ul>\n</li>\n<li class=\"toctree-l1\"><a class=\"reference internal\" href=\"i18n/\">Internationalization</a><ul>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"i18n/#making-strings-localizable\">Making Strings Localizable</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"i18n/#strings-in-templates\">Strings in Templates</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"i18n/#strings-in-python\">Strings in Python</a></li>\n</ul>\n</li>\n<li class=\"toctree-l1\"><a class=\"reference internal\" href=\"i18n/#administrative-tasks\">Administrative Tasks</a><ul>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"i18n/#updating-localization-files\">Updating Localization Files</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"i18n/#compiling-to-mo\">Compiling to MO</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"i18n/#transifex-integration\">Transifex Integration</a></li>\n</ul>\n</li>\n<li class=\"toctree-l1\"><a class=\"reference internal\" href=\"api/\">Read the Docs Public API</a><ul>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/#a-basic-api-client-using-slumber\">A basic API client using slumber</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/#example-of-adding-a-user-to-a-project\">Example of adding a user to a project</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/#api-endpoints\">API Endpoints</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/#root\">Root</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/#builds\">Builds</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/#build\">Build</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/#files\">Files</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/#file\">File</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/#projects\">Projects</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/#project\">Project</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/#users\">Users</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/#user\">User</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/#versions\">Versions</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/#version\">Version</a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/#filtering-examples\">Filtering Examples</a></li>\n</ul>\n</li>\n<li class=\"toctree-l1\"><a class=\"reference internal\" href=\"api/\">API</a><ul>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/bookmarks/\"><tt class=\"docutils literal\"><span class=\"pre\">bookmarks</span></tt></a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/builds/\"><tt class=\"docutils literal\"><span class=\"pre\">builds</span></tt></a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/doc_builder/\"><tt class=\"docutils literal\"><span class=\"pre\">doc_builder</span></tt></a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/core/\"><tt class=\"docutils literal\"><span class=\"pre\">core</span></tt></a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/projects/\"><tt class=\"docutils literal\"><span class=\"pre\">projects</span></tt></a></li>\n<li class=\"toctree-l2\"><a class=\"reference internal\" href=\"api/vcs_support/\"><tt class=\"docutils literal\"><span class=\"pre\">vcs_support</span></tt></a></li>\n</ul>\n</li>\n</ul>\n</div>\n",
                            "version": "latest",
                            "path": "index",
                            "page_id": "developer-documentation"
                        },
                        "highlight": {
                            "content": [
                                " class=\"reference internal\" href=\"<em>install</em>/\">Installation</a><ul>\n<li class=\"toctree-l2\"><a class",
                                "=\"reference internal\" href=\"<em>install</em>/#solr-search-setup\">Solr (Search) Setup</a></li>\n<li class=\"toctree-l2",
                                "\"><a class=\"reference internal\" href=\"<em>install</em>/#what-s-available\">What\u2019s available</a></li>\n</ul",
                                "-<em>install</em>\">USE_PIP_<em>INSTALL</em></a></li>\n</ul>\n</li>\n<li class=\"toctree-l1\"><a class=\"reference internal"
                            ]
                        },
                        "_id": "9e0902a4ad18dd5a61fa5a76f521a281"
                    },
                    {
                        "_type": "section",
                        "_index": "readthedocs-20131026230446",
                        "_score": 0.13945901,
                        "fields": {
                            "project": "docs",
                            "title": "Write Your Docs",
                            "content": "\n<h2>Write Your Docs<a class=\"headerlink\" href=\"#write-your-docs\" title=\"Permalink to this headline\">\u00b6</a></h2>\n<p>Install <a class=\"reference external\" href=\"http://sphinx.pocoo.org/\">Sphinx</a>, and create a directory inside your project to hold your docs:</p>\n<div class=\"highlight-python\"><pre>$ cd /path/to/project\n$ mkdir docs</pre>\n</div>\n<p>Run <tt class=\"docutils literal\"><span class=\"pre\">sphinx-quickstart</span></tt> in there:</p>\n<div class=\"highlight-python\"><pre>$ cd docs\n$ sphinx-quickstart</pre>\n</div>\n<p>This will walk you through creating the basic configuration; in most cases, you\ncan just accept the defaults. When it\u2019s done, you\u2019ll have an <tt class=\"docutils literal\"><span class=\"pre\">index.rst</span></tt>, a\n<tt class=\"docutils literal\"><span class=\"pre\">conf.py</span></tt> and some other files. Add these to revision control.</p>\n<p>Now, edit your <tt class=\"docutils literal\"><span class=\"pre\">index.rst</span></tt> and add some information about your project.\nInclude as much detail as you like (refer to the <a class=\"reference external\" href=\"http://sphinx.pocoo.org/rest.html\">reStructuredText</a> syntax\nif you need help). Build them to see how they look:</p>\n<div class=\"highlight-python\"><pre>$ make html</pre>\n</div>\n<p>Edit and rebuild until you like what you see, then commit and/or push your\nchanges to your public repository.</p>\n",
                            "version": "latest",
                            "path": "getting_started",
                            "page_id": "write-your-docs"
                        },
                        "highlight": {
                            "content": [
                                "\">\u00b6</a></h2>\n<p><em>Install</em> <a class=\"reference external\" href=\"http://sphinx.pocoo.org/\">Sphinx</a"
                            ]
                        },
                        "_id": "0eca75a4148989dc1ef660bc4a5d7b50"
                    },
                    {
                        "_type": "section",
                        "_index": "readthedocs-20131026230446",
                        "_score": 0.119536296,
                        "fields": {
                            "project": "docs",
                            "title": "My project isn\u2019t building with autodoc",
                            "content": "\n<h2>My project isn\u2019t building with autodoc<a class=\"headerlink\" href=\"#my-project-isn-t-building-with-autodoc\" title=\"Permalink to this headline\">\u00b6</a></h2>\n<p>First, you should check out the Builds tab of your project. That records all of the build attempts that RTD has made to build your project. If you see <tt class=\"docutils literal\"><span class=\"pre\">ImportError</span></tt> messages for custom Python modules, you should enable the virtualenv feature in the Admin page of your project, which will install your project into a virtualenv, and allow you to specify a <tt class=\"docutils literal\"><span class=\"pre\">requirements.txt</span></tt> file for your project.</p>\n<p>If you are still seeing errors because of C library dependencies, please see the below section about that.</p>\n",
                            "version": "latest",
                            "path": "faq",
                            "page_id": "my-project-isn-t-building-with-autodoc"
                        },
                        "highlight": {
                            "content": [
                                ", which will <em>install</em> your project into a virtualenv, and allow you to specify a <tt class=\"docutils"
                            ]
                        },
                        "_id": "68d1c98cb53f20f27d7511728b1de32a"
                    },
                    {
                        "_type": "section",
                        "_index": "readthedocs-20131026230446",
                        "_score": 0.119536296,
                        "fields": {
                            "project": "docs",
                            "title": "Packages installed in the build environment",
                            "content": "\n<h2>Packages installed in the build environment<a class=\"headerlink\" href=\"#packages-installed-in-the-build-environment\" title=\"Permalink to this headline\">\u00b6</a></h2>\n<p>The build server does have a select number of C libraries installed, because they are used across a wide array of python projects. We can\u2019t install every C library out there, but we try and support the major ones. We currently have the following libraries installed:</p>\n<blockquote>\n<div><ul class=\"simple\">\n<li>Latex (texlive-full)</li>\n<li>libevent (libevent-dev)</li>\n<li>dvipng</li>\n<li>graphviz</li>\n<li>libxslt1.1</li>\n<li>libxml2-dev</li>\n</ul>\n</div></blockquote>\n",
                            "version": "latest",
                            "path": "builds",
                            "page_id": "packages-installed-in-the-build-environment"
                        },
                        "highlight": {
                            "content": [
                                " projects. We can\u2019t <em>install</em> every C library out there, but we try and support the major ones. We currently"
                            ]
                        },
                        "_id": "749b166031453a4ec55cb0a0f2964152"
                    },
                    {
                        "_type": "section",
                        "_index": "readthedocs-20131026230446",
                        "_score": 0.079690866,
                        "fields": {
                            "project": "docs",
                            "title": "Solr (Search) Setup",
                            "content": "\n<h2>Solr (Search) Setup<a class=\"headerlink\" href=\"#solr-search-setup\" title=\"Permalink to this headline\">\u00b6</a></h2>\n<p>Apache Solr is used to index and search documents.</p>\n<p>Additional python requirements necessary to use Solr:</p>\n<div class=\"highlight-python\"><pre>pip install pysolr\npip install pyquery</pre>\n</div>\n<p>Fetch and unpack Solr:</p>\n<div class=\"highlight-python\"><pre>curl -O http://archive.apache.org/dist/lucene/solr/3.5.0/apache-solr-3.5.0.tgz\ntar xvzf apache-solr-3.5.0.tgz &amp;&amp; SOLR_PATH=`pwd`/apache-solr-3.5.0/example</pre>\n</div>\n<p>Generate the schema.xml file:</p>\n<div class=\"highlight-python\"><pre>./manage.py build_solr_schema &gt; $SOLR_PATH/solr/conf/schema.xml</pre>\n</div>\n<p>Start the server:</p>\n<div class=\"highlight-python\"><pre>cd $SOLR_PATH &amp;&amp; java -jar start.jar</pre>\n</div>\n<p>Index the data:</p>\n<div class=\"highlight-python\"><pre>./manage.py build_files # creates database objects referencing project files\n./manage.py update_index</pre>\n</div>\n<div class=\"admonition note\">\n<p class=\"first admonition-title\">Note</p>\n<p>For production environments, you\u2019ll want to run Solr in a more permanent\nservelet container, such as Tomcat or Jetty. Ubuntu distributions include\nprepackaged Solr installations. Try <tt class=\"docutils literal\"><span class=\"pre\">aptitude</span> <span class=\"pre\">install</span> <span class=\"pre\">solr-tomcat</span></tt> or\n<tt class=\"docutils literal\"><span class=\"pre\">aptitude</span> <span class=\"pre\">install</span> <span class=\"pre\">solr-jetty.</span></tt></p>\n<p class=\"last\">See /etc/[solr|tomcat6|jetty] for configuration options.  The <tt class=\"docutils literal\"><span class=\"pre\">schema.xml</span></tt>\nfile must be replaced with the version built by django-haystack.</p>\n</div>\n",
                            "version": "latest",
                            "path": "install",
                            "page_id": "solr-search-setup"
                        },
                        "highlight": {
                            "content": [
                                " requirements necessary to use Solr:</p>\n<div class=\"highlight-python\"><pre>pip <em>install</em> pysolr\npip",
                                " <em>install</em> pyquery</pre>\n</div>\n<p>Fetch and unpack Solr:</p>\n<div class=\"highlight-python\"><pre>curl -O",
                                "\"><span class=\"pre\">aptitude</span> <span class=\"pre\"><em>install</em></span> <span class=\"pre\">solr-tomcat</span",
                                "></tt> or\n<tt class=\"docutils literal\"><span class=\"pre\">aptitude</span> <span class=\"pre\"><em>install</em>"
                            ]
                        },
                        "_id": "ae4c9e1dd2d667524146913e3eab5b74"
                    },
                    {
                        "_type": "section",
                        "_index": "readthedocs-20131026230446",
                        "_score": 0.017432377,
                        "fields": {
                            "project": "docs",
                            "title": "Have a local settings file",
                            "content": "\n<h2>Have a local settings file<a class=\"headerlink\" href=\"#have-a-local-settings-file\" title=\"Permalink to this headline\">\u00b6</a></h2>\n<p>If you put a file named <tt class=\"docutils literal\"><span class=\"pre\">local_settings.py</span></tt> in the <tt class=\"docutils literal\"><span class=\"pre\">readthedocs/settings</span></tt> directory, it will override settings available in the base install.</p>\n",
                            "version": "latest",
                            "path": "custom_installs/customization",
                            "page_id": "have-a-local-settings-file"
                        },
                        "highlight": {
                            "content": [
                                "\">readthedocs/settings</span></tt> directory, it will override settings available in the base <em>install</em>.</p>\n"
                            ]
                        },
                        "_id": "2eda2a4b864ec19cd882edb5183f49b2"
                    },
                    {
                        "_type": "section",
                        "_index": "readthedocs-20131026230446",
                        "_score": 0.00440234,
                        "fields": {
                            "project": "docs",
                            "title": "Filtering Examples",
                            "content": "\n<h2>Filtering Examples<a class=\"headerlink\" href=\"#filtering-examples\" title=\"Permalink to this headline\">\u00b6</a></h2>\n<div class=\"section\" id=\"find-highest-version\">\n<h3>Find Highest Version<a class=\"headerlink\" href=\"#find-highest-version\" title=\"Permalink to this headline\">\u00b6</a></h3>\n<div class=\"highlight-python\"><pre>http://readthedocs.org/api/v1/version/pip/highest/?format=json</pre>\n</div>\n<dl class=\"method\">\n<dt id=\"method-get-api-v1-version-id-highest-\">\n<tt class=\"descclassname deschttpmethod\">GET </tt><tt class=\"descname deschttpurl\"><span class=\"deschttppath\">/api/v1/version/<em class=\"deschttppatharg\">{<span class=\"deschttppatharg deschttppatharg\">id</span>}</em>/highest/</span></tt><a class=\"headerlink\" href=\"#method-get-api-v1-version-id-highest-\" title=\"Permalink to this definition\">\u00b6</a></dt>\n<dd><table class=\"docutils field-list\" frame=\"void\" rules=\"none\">\n<col class=\"field-name\"/>\n<col class=\"field-body\"/>\n<tbody valign=\"top\">\n<tr class=\"field-odd field\"><th class=\"field-name\">Path arguments:</th><td class=\"field-body\"><strong>id</strong> \u2013 A Version id.</td>\n</tr>\n</tbody>\n</table>\n</dd></dl>\n\n<dl class=\"response\">\n<dt id=\"response-retrieve-highest-version\">\n<strong class=\"deschttpresponse\">Retrieve highest version.</strong><a class=\"headerlink\" href=\"#response-retrieve-highest-version\" title=\"Permalink to this definition\">\u00b6</a></dt>\n<dd><div class=\"highlight-js\"><div class=\"highlight\"><pre><span class=\"p\">{</span>\n    <span class=\"s2\">\"is_highest\"</span><span class=\"o\">:</span> <span class=\"kc\">true</span><span class=\"p\">,</span>\n    <span class=\"s2\">\"project\"</span><span class=\"o\">:</span> <span class=\"s2\">\"Version 1.0.1 of pip (5476)\"</span><span class=\"p\">,</span>\n    <span class=\"s2\">\"slug\"</span><span class=\"o\">:</span> <span class=\"p\">[</span>\n        <span class=\"s2\">\"1.0.1\"</span>\n    <span class=\"p\">],</span>\n    <span class=\"s2\">\"url\"</span><span class=\"o\">:</span> <span class=\"s2\">\"/docs/pip/en/1.0.1/\"</span><span class=\"p\">,</span>\n    <span class=\"s2\">\"version\"</span><span class=\"o\">:</span> <span class=\"s2\">\"1.0.1\"</span>\n<span class=\"p\">}</span>\n</pre></div>\n</div>\n</dd></dl>\n\n</div>\n<div class=\"section\" id=\"compare-highest-version\">\n<h3>Compare Highest Version<a class=\"headerlink\" href=\"#compare-highest-version\" title=\"Permalink to this headline\">\u00b6</a></h3>\n<p>This will allow you to compare whether a certain version is the highest version of a specific project. The below query should return a <tt class=\"xref py py-obj docutils literal\"><span class=\"pre\">'is_highest':</span> <span class=\"pre\">false</span></tt> in the returned dictionary.</p>\n<div class=\"highlight-python\"><pre>http://readthedocs.org/api/v1/version/pip/highest/0.8/?format=json</pre>\n</div>\n<dl class=\"method\">\n<dt id=\"method-get-api-v1-version-id-highest-version-\">\n<tt class=\"descclassname deschttpmethod\">GET </tt><tt class=\"descname deschttpurl\"><span class=\"deschttppath\">/api/v1/version/<em class=\"deschttppatharg\">{<span class=\"deschttppatharg deschttppatharg\">id</span>}</em>/highest/<em class=\"deschttppatharg\">{<span class=\"deschttppatharg deschttppatharg\">version</span>}</em></span></tt><a class=\"headerlink\" href=\"#method-get-api-v1-version-id-highest-version-\" title=\"Permalink to this definition\">\u00b6</a></dt>\n<dd><table class=\"docutils field-list\" frame=\"void\" rules=\"none\">\n<col class=\"field-name\"/>\n<col class=\"field-body\"/>\n<tbody valign=\"top\">\n<tr class=\"field-odd field\"><th class=\"field-name\">Path arguments:</th><td class=\"field-body\"><ul class=\"first last simple\">\n<li><strong>id</strong> \u2013 A Version id.</li>\n<li><strong>version</strong> \u2013 A Version number or string.</li>\n</ul>\n</td>\n</tr>\n</tbody>\n</table>\n</dd></dl>\n\n<dl class=\"response\">\n<dt>\n<strong class=\"deschttpresponse\">Retrieve highest version.</strong></dt>\n<dd><div class=\"highlight-js\"><div class=\"highlight\"><pre><span class=\"p\">{</span>\n    <span class=\"s2\">\"is_highest\"</span><span class=\"o\">:</span> <span class=\"kc\">false</span><span class=\"p\">,</span>\n    <span class=\"s2\">\"project\"</span><span class=\"o\">:</span> <span class=\"s2\">\"Version 1.0.1 of pip (5476)\"</span><span class=\"p\">,</span>\n    <span class=\"s2\">\"slug\"</span><span class=\"o\">:</span> <span class=\"p\">[</span>\n        <span class=\"s2\">\"1.0.1\"</span>\n    <span class=\"p\">],</span>\n    <span class=\"s2\">\"url\"</span><span class=\"o\">:</span> <span class=\"s2\">\"/docs/pip/en/1.0.1/\"</span><span class=\"p\">,</span>\n    <span class=\"s2\">\"version\"</span><span class=\"o\">:</span> <span class=\"s2\">\"1.0.1\"</span>\n<span class=\"p\">}</span>\n</pre></div>\n</div>\n</dd></dl>\n\n</div>\n<div class=\"section\" id=\"file-search\">\n<h3>File Search<a class=\"headerlink\" href=\"#file-search\" title=\"Permalink to this headline\">\u00b6</a></h3>\n<div class=\"highlight-python\"><pre>http://readthedocs.org/api/v1/file/search/?format=json&amp;q=virtualenvwrapper</pre>\n</div>\n<dl class=\"method\">\n<dt id=\"method-get-api-v1-file-search-q-search_term-\">\n<tt class=\"descclassname deschttpmethod\">GET </tt><tt class=\"descname deschttpurl\"><span class=\"deschttppath\">/api/v1/file/search/</span><span class=\"deschttpquery\">?<em class=\"deschttpqueryparam\">q={search_term}</em></span></tt><a class=\"headerlink\" href=\"#method-get-api-v1-file-search-q-search_term-\" title=\"Permalink to this definition\">\u00b6</a></dt>\n<dd><table class=\"docutils field-list\" frame=\"void\" rules=\"none\">\n<col class=\"field-name\"/>\n<col class=\"field-body\"/>\n<tbody valign=\"top\">\n<tr class=\"field-odd field\"><th class=\"field-name\">Path arguments:</th><td class=\"field-body\"><strong>search_term</strong> \u2013 Perform search with this term.</td>\n</tr>\n</tbody>\n</table>\n</dd></dl>\n\n<dl class=\"response\">\n<dt id=\"response-retrieve-a-list-of-file-objects-that-contain-the-search-term\">\n<strong class=\"deschttpresponse\">Retrieve a list of File objects that contain the search term.</strong><a class=\"headerlink\" href=\"#response-retrieve-a-list-of-file-objects-that-contain-the-search-term\" title=\"Permalink to this definition\">\u00b6</a></dt>\n<dd><div class=\"highlight-js\"><div class=\"highlight\"><pre><span class=\"p\">{</span>\n    <span class=\"s2\">\"objects\"</span><span class=\"o\">:</span> <span class=\"p\">[</span>\n        <span class=\"p\">{</span>\n            <span class=\"s2\">\"absolute_url\"</span><span class=\"o\">:</span> <span class=\"s2\">\"/docs/python-guide/en/latest/scenarios/virtualenvs/index.html\"</span><span class=\"p\">,</span>\n            <span class=\"s2\">\"id\"</span><span class=\"o\">:</span> <span class=\"s2\">\"375539\"</span><span class=\"p\">,</span>\n            <span class=\"s2\">\"name\"</span><span class=\"o\">:</span> <span class=\"s2\">\"index.html\"</span><span class=\"p\">,</span>\n            <span class=\"s2\">\"path\"</span><span class=\"o\">:</span> <span class=\"s2\">\"scenarios/virtualenvs/index.html\"</span><span class=\"p\">,</span>\n            <span class=\"s2\">\"project\"</span><span class=\"o\">:</span> <span class=\"p\">{</span>\n                <span class=\"s2\">\"absolute_url\"</span><span class=\"o\">:</span> <span class=\"s2\">\"/projects/python-guide/\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"analytics_code\"</span><span class=\"o\">:</span> <span class=\"kc\">null</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"copyright\"</span><span class=\"o\">:</span> <span class=\"s2\">\"Unknown\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"crate_url\"</span><span class=\"o\">:</span> <span class=\"s2\">\"\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"default_branch\"</span><span class=\"o\">:</span> <span class=\"s2\">\"\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"default_version\"</span><span class=\"o\">:</span> <span class=\"s2\">\"latest\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"description\"</span><span class=\"o\">:</span> <span class=\"s2\">\"[WIP] Python best practices...\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"django_packages_url\"</span><span class=\"o\">:</span> <span class=\"s2\">\"\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"documentation_type\"</span><span class=\"o\">:</span> <span class=\"s2\">\"sphinx_htmldir\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"id\"</span><span class=\"o\">:</span> <span class=\"s2\">\"530\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"modified_date\"</span><span class=\"o\">:</span> <span class=\"s2\">\"2012-03-13T01:05:30.191496\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"name\"</span><span class=\"o\">:</span> <span class=\"s2\">\"python-guide\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"project_url\"</span><span class=\"o\">:</span> <span class=\"s2\">\"\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"pub_date\"</span><span class=\"o\">:</span> <span class=\"s2\">\"2011-03-20T19:40:03.599987\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"repo\"</span><span class=\"o\">:</span> <span class=\"s2\">\"git://github.com/kennethreitz/python-guide.git\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"repo_type\"</span><span class=\"o\">:</span> <span class=\"s2\">\"git\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"requirements_file\"</span><span class=\"o\">:</span> <span class=\"s2\">\"\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"resource_uri\"</span><span class=\"o\">:</span> <span class=\"s2\">\"/api/v1/project/530/\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"slug\"</span><span class=\"o\">:</span> <span class=\"s2\">\"python-guide\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"subdomain\"</span><span class=\"o\">:</span> <span class=\"s2\">\"http://python-guide.readthedocs.org/\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"suffix\"</span><span class=\"o\">:</span> <span class=\"s2\">\".rst\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"theme\"</span><span class=\"o\">:</span> <span class=\"s2\">\"kr\"</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"use_virtualenv\"</span><span class=\"o\">:</span> <span class=\"kc\">false</span><span class=\"p\">,</span>\n                <span class=\"s2\">\"users\"</span><span class=\"o\">:</span> <span class=\"p\">[</span>\n                    <span class=\"s2\">\"/api/v1/user/130/\"</span>\n                <span class=\"p\">],</span>\n                <span class=\"s2\">\"version\"</span><span class=\"o\">:</span> <span class=\"s2\">\"\"</span>\n            <span class=\"p\">},</span>\n            <span class=\"s2\">\"resource_uri\"</span><span class=\"o\">:</span> <span class=\"s2\">\"/api/v1/file/375539/\"</span><span class=\"p\">,</span>\n            <span class=\"s2\">\"text\"</span><span class=\"o\">:</span> <span class=\"s2\">\"...&lt;span class=\\\"highlighted\\\"&gt;virtualenvwrapper&lt;/span&gt;\\n...\"</span>\n        <span class=\"p\">},</span>\n        <span class=\"p\">...</span>\n    <span class=\"p\">]</span>\n<span class=\"p\">}</span>\n</pre></div>\n</div>\n</dd></dl>\n\n</div>\n<div class=\"section\" id=\"anchor-search\">\n<h3>Anchor Search<a class=\"headerlink\" href=\"#anchor-search\" title=\"Permalink to this headline\">\u00b6</a></h3>\n<div class=\"highlight-python\"><pre>http://readthedocs.org/api/v1/file/anchor/?format=json&amp;q=virtualenv</pre>\n</div>\n<dl class=\"method\">\n<dt id=\"method-get-api-v1-file-anchor-q-search_term-\">\n<tt class=\"descclassname deschttpmethod\">GET </tt><tt class=\"descname deschttpurl\"><span class=\"deschttppath\">/api/v1/file/anchor/</span><span class=\"deschttpquery\">?<em class=\"deschttpqueryparam\">q={search_term}</em></span></tt><a class=\"headerlink\" href=\"#method-get-api-v1-file-anchor-q-search_term-\" title=\"Permalink to this definition\">\u00b6</a></dt>\n<dd><table class=\"docutils field-list\" frame=\"void\" rules=\"none\">\n<col class=\"field-name\"/>\n<col class=\"field-body\"/>\n<tbody valign=\"top\">\n<tr class=\"field-odd field\"><th class=\"field-name\">Path arguments:</th><td class=\"field-body\"><strong>search_term</strong> \u2013 Perform search of files containing anchor text with this term.</td>\n</tr>\n</tbody>\n</table>\n</dd></dl>\n\n<dl class=\"response\">\n<dt id=\"response-retrieve-a-list-of-absolute-uris-for-files-that-contain-the-search-term\">\n<strong class=\"deschttpresponse\">Retrieve a list of absolute URIs for files that contain the search term.</strong><a class=\"headerlink\" href=\"#response-retrieve-a-list-of-absolute-uris-for-files-that-contain-the-search-term\" title=\"Permalink to this definition\">\u00b6</a></dt>\n<dd><div class=\"highlight-js\"><div class=\"highlight\"><pre><span class=\"p\">{</span>\n    <span class=\"s2\">\"objects\"</span><span class=\"o\">:</span> <span class=\"p\">[</span>\n        <span class=\"s2\">\"http//django-fab-deploy.readthedocs.org/en/latest/...\"</span><span class=\"p\">,</span>\n        <span class=\"s2\">\"http//dimagi-deployment-tools.readthedocs.org/en/...\"</span><span class=\"p\">,</span>\n        <span class=\"s2\">\"http//openblock.readthedocs.org/en/latest/install/base_install.html#virtualenv\"</span><span class=\"p\">,</span>\n        <span class=\"p\">...</span>\n    <span class=\"p\">]</span>\n<span class=\"p\">}</span>\n</pre></div>\n</div>\n</dd></dl>\n\n</div>\n",
                            "version": "latest",
                            "path": "api",
                            "page_id": "filtering-examples"
                        },
                        "highlight": {
                            "content": [
                                "/<em>install</em>/base_<em>install</em>.html#virtualenv\"</span><span class=\"p\">,</span>\n        <span class=\"p\">...</span"
                            ]
                        },
                        "_id": "a6d4a7689edffea95f782c51c50e0794"
                    }
                ],
                "total": 9,
                "max_score": 396.33047
            },
            "_shards": {
                "successful": 1,
                "failed": 0,
                "total": 1
            },
            "took": 133,
            "facets": {
                "path": {
                    "_type": "terms",
                    "total": 34,
                    "terms": [
                        {
                            "count": 5,
                            "term": "contents/installation"
                        },
                        {
                            "count": 4,
                            "term": "install"
                        },
                        {
                            "count": 4,
                            "term": "index"
                        },
                        {
                            "count": 2,
                            "term": "start/installing"
                        },
                        {
                            "count": 2,
                            "term": "quickstart"
                        },
                        {
                            "count": 2,
                            "term": "dev/index"
                        },
                        {
                            "count": 2,
                            "term": "contributing"
                        },
                        {
                            "count": 2,
                            "term": "contents/code"
                        },
                        {
                            "count": 1,
                            "term": "settings"
                        },
                        {
                            "count": 1,
                            "term": "getting_started"
                        }
                    ],
                    "other": 9,
                    "missing": 0
                }
            },
            "timed_out": False
        }
    })

