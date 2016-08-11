



<!DOCTYPE html>
<html lang="en" class=" is-copy-enabled emoji-size-boost is-u2f-enabled">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    

    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-be4c6e0e479a2d4d0eb3159c8772b5bfc4aa39831cb28f5f92cc2e448d93eaa1.css" integrity="sha256-vkxuDkeaLU0OsxWch3K1v8SqOYMcso9fkswuRI2T6qE=" media="all" rel="stylesheet" />
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-74799a246b311c7844ffbe1b262207ee8b1fd3edb94ac8f16770f80e97720879.css" integrity="sha256-dHmaJGsxHHhE/74bJiIH7osf0+25SsjxZ3D4DpdyCHk=" media="all" rel="stylesheet" />
    
    
    
    

    <link as="script" href="https://assets-cdn.github.com/assets/frameworks-efdb851061bb7933d0e409f8be67f6ae483a2fa8612b913ae2678aa4abf4569a.js" rel="preload" />
    
    <link as="script" href="https://assets-cdn.github.com/assets/github-8cefd4d3873fd29d8173f9b396fc15c35fde209962f937c739072971fb4a62c3.js" rel="preload" />

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=device-width">
    
    <title>python-ecology-lesson/00-short-introduction-to-Python.md at gh-pages · aschoenr/python-ecology-lesson</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="/apple-touch-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="/apple-touch-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="/apple-touch-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="/apple-touch-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon-180x180.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="https://avatars2.githubusercontent.com/u/20911370?v=3&amp;s=400" name="twitter:image:src" /><meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="aschoenr/python-ecology-lesson" name="twitter:title" /><meta content="Contribute to python-ecology-lesson development by creating an account on GitHub." name="twitter:description" />
      <meta content="https://avatars2.githubusercontent.com/u/20911370?v=3&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="aschoenr/python-ecology-lesson" property="og:title" /><meta content="https://github.com/aschoenr/python-ecology-lesson" property="og:url" /><meta content="Contribute to python-ecology-lesson development by creating an account on GitHub." property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/MjA5MTEzNzA6NzZhMGIwOGNkZTQ5MjE2ZWQ5MDM2ZWEyNTJlMDE1ZGQ6M2QxODRhMTI5YWY3ZWMzNmRmZjg3ZjJiYWM0ODRhMTM0Mjk1ZDE5NGMzZjUzMzdjY2QzYjEyZjVlMDQ4ZWNhNw==--6c80b91afe418f6c5822fbcff2d92aa737623edb">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">
    <meta name="request-id" content="86756824:2554C:FD4B0E:57ACD7E3" data-pjax-transient>

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="86756824:2554C:FD4B0E:57ACD7E3" name="octolytics-dimension-request_id" /><meta content="20911370" name="octolytics-actor-id" /><meta content="aschoenr" name="octolytics-actor-login" /><meta content="b11b1062e2c605cf878c731da127ce4fa5d4176529f9782c46bb9cf40c148d2e" name="octolytics-actor-hash" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />



  <meta class="js-ga-set" name="dimension1" content="Logged In">



        <meta name="hostname" content="github.com">
    <meta name="user-login" content="aschoenr">

        <meta name="expected-hostname" content="github.com">
      <meta name="js-proxy-site-detection-payload" content="YjlkMWQzMWFiMWNmODlmZTBiOTBhZWQ2ZDdhNzE3MzZlMjk4MDNkNTU2MTRlOTEzMDQzYjFiNjJjODQ1ODNkMHx7InJlbW90ZV9hZGRyZXNzIjoiMTM0LjExNy4xMDQuMzYiLCJyZXF1ZXN0X2lkIjoiODY3NTY4MjQ6MjU1NEM6RkQ0QjBFOjU3QUNEN0UzIiwidGltZXN0YW1wIjoxNDcwOTQ1MjU1fQ==">


      <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#4078c0">
      <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

    <meta name="html-safe-nonce" content="183c9d49fa23f46b85fd154356e1ac5c350efd39">
    <meta content="3bfda747cb007061e7608fed7b01a5cc1b347f86" name="form-nonce" />

    <meta http-equiv="x-pjax-version" content="88e57562bb41131567dbb201d846b402">
    

      
  <meta name="description" content="Contribute to python-ecology-lesson development by creating an account on GitHub.">
  <meta name="go-import" content="github.com/aschoenr/python-ecology-lesson git https://github.com/aschoenr/python-ecology-lesson.git">

  <meta content="20911370" name="octolytics-dimension-user_id" /><meta content="aschoenr" name="octolytics-dimension-user_login" /><meta content="65495871" name="octolytics-dimension-repository_id" /><meta content="aschoenr/python-ecology-lesson" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="65495871" name="octolytics-dimension-repository_network_root_id" /><meta content="aschoenr/python-ecology-lesson" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/aschoenr/python-ecology-lesson/commits/gh-pages.atom" rel="alternate" title="Recent Commits to python-ecology-lesson:gh-pages" type="application/atom+xml">


      <link rel="canonical" href="https://github.com/aschoenr/python-ecology-lesson/blob/gh-pages/00-short-introduction-to-Python.md" data-pjax-transient>
  </head>


  <body class="logged-in  env-production macintosh vis-public page-blob">
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>

    
    
    



        <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg aria-hidden="true" class="octicon octicon-mark-github" height="28" version="1.1" viewBox="0 0 16 16" width="28"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>


        <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/aschoenr/python-ecology-lesson/search" class="js-site-search-form" data-scoped-search-url="/aschoenr/python-ecology-lesson/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
      <div class="header-search-scope">This repository</div>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
    </label>
</form></div>


      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item">
          <a href="/pulls" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
            Pull requests
</a>        </li>
        <li class="header-nav-item">
          <a href="/issues" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
            Issues
</a>        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com/" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item">
    

  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link tooltipped tooltipped-s js-menu-target" href="/new"
       aria-label="Create new…"
       data-ga-click="Header, create new, icon:add">
      <svg aria-hidden="true" class="octicon octicon-plus left" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 9H7v5H5V9H0V7h5V2h2v5h5z"></path></svg>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>


  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="aschoenr/python-ecology-lesson">This repository</span>
  </div>
    <a class="dropdown-item" href="/aschoenr/python-ecology-lesson/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>
    <a class="dropdown-item" href="/aschoenr/python-ecology-lesson/settings/collaboration" data-ga-click="Header, create new collaborator">
      New collaborator
    </a>

      </ul>
    </div>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name tooltipped tooltipped-sw js-menu-target" href="/aschoenr"
       aria-label="View profile and more"
       data-ga-click="Header, show menu, icon:avatar">
      <img alt="@aschoenr" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/20911370?v=3&amp;s=40" width="20" />
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <div class="dropdown-menu dropdown-menu-sw">
        <div class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">aschoenr</strong>
        </div>

        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="/aschoenr" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a>
        <a class="dropdown-item" href="/stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a>
        <a class="dropdown-item" href="/explore" data-ga-click="Header, go to explore, text:explore">
          Explore
        </a>
          <a class="dropdown-item" href="/integrations" data-ga-click="Header, go to integrations, text:integrations">
            Integrations
          </a>
        <a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a>


        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a>

        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/logout" class="logout-form" data-form-nonce="3bfda747cb007061e7608fed7b01a5cc1b347f86" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="qGDL3X+RK3lrI98BBlJ8C2u1ZCP8aDaMgVs2qJhY8cF6ygaFPET22UrvDUNfc5rbxzlPejRZgv4pfbEzdxXYtg==" /></div>
          <button class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </li>
</ul>


    
  </div>
</div>


      


    <div id="start-of-content" class="accessibility-aid"></div>

      <div id="js-flash-container">
</div>


    <div role="main">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
      
<div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
  <div class="container repohead-details-container">

    

<ul class="pagehead-actions">

  <li>
        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-form-nonce="3bfda747cb007061e7608fed7b01a5cc1b347f86" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="fEWeo57FaXCRqyoToN5OLNwdIO4RbYKdBQxLCJoqmnpxbhDrgJx+DrXpOVExX3Q6jzgof1UMMxt+eKAwzKft8g==" /></div>      <input class="form-control" id="repository_id" name="repository_id" type="hidden" value="65495871" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/aschoenr/python-ecology-lesson/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
              <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
              Watch
            </span>
          </a>
          <a class="social-count js-social-count" href="/aschoenr/python-ecology-lesson/watchers">
            0
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
                  <div class="select-menu-item-text">
                    <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
                  <div class="select-menu-item-text">
                    <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
                      Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
                  <div class="select-menu-item-text">
                    <input id="do_ignore" name="do" type="radio" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-mute" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"></path></svg>
                      Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/aschoenr/python-ecology-lesson/unstar" class="starred" data-form-nonce="3bfda747cb007061e7608fed7b01a5cc1b347f86" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="NuMQ/qbYflmwcRIYoFhDfT+wL4oo8BTXYKDl+Vp8g2RC2WzvznqNpVgXQCOw5b55Spq4VhXSwfl/mZC+fcPNTA==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar aschoenr/python-ecology-lesson"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"></path></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/aschoenr/python-ecology-lesson/stargazers">
          0
        </a>
</form>
    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/aschoenr/python-ecology-lesson/star" class="unstarred" data-form-nonce="3bfda747cb007061e7608fed7b01a5cc1b347f86" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="jo4gm/77/VROk7l3LjiOjwnhULbU6InGhWUcSz8/vZeRiy2sUB1Mu/fIFT5xmSPmZZGFZhU4T5wxs5g+T8U/xQ==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star aschoenr/python-ecology-lesson"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"></path></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/aschoenr/python-ecology-lesson/stargazers">
          0
        </a>
</form>  </div>

  </li>

  <li>
          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/aschoenr/python-ecology-lesson/fork" class="btn-with-count" data-form-nonce="3bfda747cb007061e7608fed7b01a5cc1b347f86" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Q7B6oI0SkJBwhMY+frCkZRzi9SbxayO2RxGGMovf3HXef5W7KNlimt74pDGC9pyYZ6XfaBb5/Ao6eJnR2MSkBg==" /></div>
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of aschoenr/python-ecology-lesson to your account"
                aria-label="Fork your own copy of aschoenr/python-ecology-lesson to your account">
              <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
              Fork
            </button>
</form>
    <a href="/aschoenr/python-ecology-lesson/network" class="social-count">
      0
    </a>
  </li>
</ul>

    <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"></path></svg>
  <span class="author" itemprop="author"><a href="/aschoenr" class="url fn" rel="author">aschoenr</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/aschoenr/python-ecology-lesson" data-pjax="#js-repo-pjax-container">python-ecology-lesson</a></strong>

</h1>

  </div>
  <div class="container">
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/aschoenr/python-ecology-lesson" aria-selected="true" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /aschoenr/python-ecology-lesson" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"></path></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/aschoenr/python-ecology-lesson/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /aschoenr/python-ecology-lesson/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
        <span itemprop="name">Issues</span>
        <span class="counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/aschoenr/python-ecology-lesson/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /aschoenr/python-ecology-lesson/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
      <span itemprop="name">Pull requests</span>
      <span class="counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a href="/aschoenr/python-ecology-lesson/wiki" class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /aschoenr/python-ecology-lesson/wiki">
      <svg aria-hidden="true" class="octicon octicon-book" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"></path></svg>
      Wiki
</a>

  <a href="/aschoenr/python-ecology-lesson/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="pulse /aschoenr/python-ecology-lesson/pulse">
    <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0v2h3.6l.9-1.8.9 5.4L9 8.5l1.6 1.5H14V8z"></path></svg>
    Pulse
</a>
  <a href="/aschoenr/python-ecology-lesson/graphs" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors /aschoenr/python-ecology-lesson/graphs">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"></path></svg>
    Graphs
</a>
    <a href="/aschoenr/python-ecology-lesson/settings" class="js-selected-navigation-item reponav-item" data-selected-links="repo_settings repo_branch_settings hooks integration_installations /aschoenr/python-ecology-lesson/settings">
      <svg aria-hidden="true" class="octicon octicon-gear" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 8.77v-1.6l-1.94-.64-.45-1.09.88-1.84-1.13-1.13-1.81.91-1.09-.45-.69-1.92h-1.6l-.63 1.94-1.11.45-1.84-.88-1.13 1.13.91 1.81-.45 1.09L0 7.23v1.59l1.94.64.45 1.09-.88 1.84 1.13 1.13 1.81-.91 1.09.45.69 1.92h1.59l.63-1.94 1.11-.45 1.84.88 1.13-1.13-.92-1.81.47-1.09L14 8.75v.02zM7 11c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3z"></path></svg>
      Settings
</a>
</nav>

  </div>
</div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    

<a href="/aschoenr/python-ecology-lesson/blob/c4127f40d85fb1d9c4d1e9b8522768ba666105b7/00-short-introduction-to-Python.md" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:c84137fa49e3c7293febce64a3d866e9 -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu branch-select-menu js-menu-container js-select-menu left">
  <button class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">gh-pages</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Find or create a branch…" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/aschoenr/python-ecology-lesson/blob/add_function_exercise_to_episode_01/00-short-introduction-to-Python.md"
               data-name="add_function_exercise_to_episode_01"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                add_function_exercise_to_episode_01
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/aschoenr/python-ecology-lesson/blob/gh-pages/00-short-introduction-to-Python.md"
               data-name="gh-pages"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                gh-pages
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/aschoenr/python-ecology-lesson/blob/new-learning-objectives/00-short-introduction-to-Python.md"
               data-name="new-learning-objectives"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                new-learning-objectives
              </span>
            </a>
        </div>

          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/aschoenr/python-ecology-lesson/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" data-form-nonce="3bfda747cb007061e7608fed7b01a5cc1b347f86" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="wo+c8XRvSppYzIN8kl7UJpPOvTEZ5Q7DIGIHuJpdJYFg3R2ZIxrtBsOlzHIlJArXRuj/pKAoxDzLOxy6ytSFjg==" /></div>
          <svg aria-hidden="true" class="octicon octicon-git-branch select-menu-item-icon" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path d="M10 5c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v.3c-.02.52-.23.98-.63 1.38-.4.4-.86.61-1.38.63-.83.02-1.48.16-2 .45V4.72a1.993 1.993 0 0 0-1-3.72C.88 1 0 1.89 0 3a2 2 0 0 0 1 1.72v6.56c-.59.35-1 .99-1 1.72 0 1.11.89 2 2 2 1.11 0 2-.89 2-2 0-.53-.2-1-.53-1.36.09-.06.48-.41.59-.47.25-.11.56-.17.94-.17 1.05-.05 1.95-.45 2.75-1.25S8.95 7.77 9 6.73h-.02C9.59 6.37 10 5.73 10 5zM2 1.8c.66 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2C1.35 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2zm0 12.41c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm6-8c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
            <div class="select-menu-item-text">
              <span class="select-menu-item-heading">Create branch: <span class="js-new-item-name"></span></span>
              <span class="description">from ‘gh-pages’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="gh-pages">
            <input type="hidden" name="path" id="path" value="00-short-introduction-to-Python.md">
</form>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="btn-group right">
    <a href="/aschoenr/python-ecology-lesson/find/gh-pages"
          class="js-pjax-capture-input btn btn-sm"
          data-pjax
          data-hotkey="t">
      Find file
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
  </div>
  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/aschoenr/python-ecology-lesson"><span>python-ecology-lesson</span></a></span></span><span class="separator">/</span><strong class="final-path">00-short-introduction-to-Python.md</strong>
  </div>
</div>

<include-fragment class="commit-tease" src="/aschoenr/python-ecology-lesson/contributors/gh-pages/00-short-introduction-to-Python.md">
  <div>
    Fetching contributors&hellip;
  </div>

  <div class="commit-tease-contributors">
    <img alt="" class="loader-loading left" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" />
    <span class="loader-error">Cannot retrieve contributors at this time</span>
  </div>
</include-fragment>
<div class="file">
  <div class="file-header">
  <div class="file-actions">

    <div class="btn-group">
      <a href="/aschoenr/python-ecology-lesson/raw/gh-pages/00-short-introduction-to-Python.md" class="btn btn-sm " id="raw-url">Raw</a>
        <a href="/aschoenr/python-ecology-lesson/blame/gh-pages/00-short-introduction-to-Python.md" class="btn btn-sm js-update-url-with-hash">Blame</a>
      <a href="/aschoenr/python-ecology-lesson/commits/gh-pages/00-short-introduction-to-Python.md" class="btn btn-sm " rel="nofollow">History</a>
    </div>

        <a class="btn-octicon tooltipped tooltipped-nw"
           href="https://mac.github.com"
           aria-label="Open this file in GitHub Desktop"
           data-ga-click="Repository, open with desktop, type:mac">
            <svg aria-hidden="true" class="octicon octicon-device-desktop" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"></path></svg>
        </a>

        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/aschoenr/python-ecology-lesson/edit/gh-pages/00-short-introduction-to-Python.md" class="inline-form js-update-url-with-hash" data-form-nonce="3bfda747cb007061e7608fed7b01a5cc1b347f86" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="OEW2s99NWL6gySQpAu58mf56tZ1htZ+mL6z4i/Xg2oQnmYvqjUdO42riqrj2cXRSXZMOzbsXkuLtv/RjcGbuOQ==" /></div>
          <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
            aria-label="Edit this file" data-hotkey="e" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"></path></svg>
          </button>
</form>        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/aschoenr/python-ecology-lesson/delete/gh-pages/00-short-introduction-to-Python.md" class="inline-form" data-form-nonce="3bfda747cb007061e7608fed7b01a5cc1b347f86" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="mnCPn4GFB0Y974QkG4avDvW+jqN0CKd5dQCrfxUbQNaV8Wy1DLCe2akUwCl36+b8Vlj2th7LPd0l/YMSfKoxHA==" /></div>
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Delete this file" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"></path></svg>
          </button>
</form>  </div>

  <div class="file-info">
      287 lines (221 sloc)
      <span class="file-info-divider"></span>
    6.48 KB
  </div>
</div>

  
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><table data-table-type="yaml-metadata">
  <thead>
  <tr>
  <th>layout</th>

  <th>root</th>

  <th>title</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><div>lesson</div></td>

  <td><div>.</div></td>

  <td><div>Short Introduction to Programming in Python</div></td>
  </tr>
  </tbody>
</table>

<h1><a id="user-content-the-basics-of-python" class="anchor" href="#the-basics-of-python" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>The Basics of Python</h1>

<p>Python is a general purpose programming language, that supports rapid development
of scripts and applications.</p>

<p>Python's main advantages:</p>

<ul>
<li>Open Source software, supported by Python Software Foundation</li>
<li>Available on all platforms</li>
<li>"Batteries Included" philosophy - libraries for common tasks available in
standard installation</li>
<li>Supports multiple programming paradigms</li>
<li>Very large community</li>
</ul>

<h2><a id="user-content-interpreter" class="anchor" href="#interpreter" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Interpreter</h2>

<p>Python is an interpreted language. As a consequence, we can use it in two ways:</p>

<ul>
<li>Using interpreter as an "advanced calculator" in interactive mode:</li>
</ul>

<div class="highlight highlight-source-python"><pre>user:host:<span class="pl-k">~</span><span class="pl-ii">$</span> python
Python <span class="pl-c1">3.5</span>.1 (default, Oct <span class="pl-c1">23</span> <span class="pl-c1">2015</span>, <span class="pl-c1">18</span>:<span class="pl-c1">0<span class="pl-ii">5</span></span>:<span class="pl-c1">0<span class="pl-ii">6</span></span>)
[<span class="pl-c1">GCC</span> <span class="pl-c1">4.8</span>.3] on linux2
Type <span class="pl-s"><span class="pl-pds">"</span>help<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>copyright<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>credits<span class="pl-pds">"</span></span> <span class="pl-k">or</span> <span class="pl-s"><span class="pl-pds">"</span>license<span class="pl-pds">"</span></span> <span class="pl-k">for</span> more information.
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> <span class="pl-c1">2</span> <span class="pl-k">+</span> <span class="pl-c1">2</span>
<span class="pl-c1">4</span>
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">"</span>Hello World<span class="pl-pds">"</span></span>)
Hello World</pre></div>

<ul>
<li>Executing programs/scripts saved as a text file, usually with <code>*.py</code> extension:</li>
</ul>

<pre><code>user:host:~$ python my_script.py
Hello World
</code></pre>

<h2><a id="user-content-introduction-to-python-built-in-data-types" class="anchor" href="#introduction-to-python-built-in-data-types" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Introduction to Python built-in data types</h2>

<h3><a id="user-content-strings-integers-and-floats" class="anchor" href="#strings-integers-and-floats" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Strings, integers and floats</h3>

<p>The most basic data types in Python are strings, integers and floats:</p>

<div class="highlight highlight-source-python"><pre>text <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">"</span>Data Carpentry<span class="pl-pds">"</span></span>
number <span class="pl-k">=</span> <span class="pl-c1">42</span>
pi_value <span class="pl-k">=</span> <span class="pl-c1">3.1415</span></pre></div>

<p>Here we've assigned data to variables, namely <code>text</code>, <code>number</code> and <code>pi_value</code>,
using the assignment operator <code>=</code>. The variable called <code>text</code> is a string which
means it can contain letters and numbers. We could reassign the variable <code>text</code>
to an integer too - but be careful reassigning variables as this can get 
confusing.</p>

<p>To print out the value stored in a variable we can simply type the name of the
variable into the interpreter:</p>

<div class="highlight highlight-source-python"><pre><span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> text
<span class="pl-s"><span class="pl-pds">"</span>Data Carpentry<span class="pl-pds">"</span></span></pre></div>

<p>however, in scripts we must use the <code>print</code> function:</p>

<div class="highlight highlight-source-python"><pre><span class="pl-c"># Comments start with #</span>
<span class="pl-c"># Next line will print out text</span>
<span class="pl-c1">print</span>(text)
<span class="pl-s"><span class="pl-pds">"</span>Data Carpentry<span class="pl-pds">"</span></span></pre></div>

<h3><a id="user-content-operators" class="anchor" href="#operators" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Operators</h3>

<p>We can perform mathematical calculations in Python using the basic operators
 <code>+, -, /, *, %</code>:</p>

<div class="highlight highlight-source-python"><pre><span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> <span class="pl-c1">2</span> <span class="pl-k">+</span> <span class="pl-c1">2</span>
<span class="pl-c1">4</span>
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> <span class="pl-c1">6</span> <span class="pl-k">*</span> <span class="pl-c1">7</span>
<span class="pl-c1">42</span>
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> <span class="pl-c1">2</span> <span class="pl-k">**</span> <span class="pl-c1">16</span>  <span class="pl-c"># power</span>
<span class="pl-c1">65536</span>
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> <span class="pl-c1">13</span> <span class="pl-k">%</span> <span class="pl-c1">5</span>  <span class="pl-c"># modulo</span>
<span class="pl-c1">3</span></pre></div>

<p>We can also use comparison and logic operators:
<code>&lt;, &gt;, ==, !=, &lt;=, &gt;=</code> etc.
<code>and, or, not</code></p>

<div class="highlight highlight-source-python"><pre><span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> <span class="pl-c1">3</span> <span class="pl-k">&gt;</span> <span class="pl-c1">4</span>
<span class="pl-c1">False</span>
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> <span class="pl-c1">True</span> <span class="pl-k">and</span> <span class="pl-c1">True</span>
<span class="pl-c1">True</span>
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> <span class="pl-c1">True</span> <span class="pl-k">or</span> <span class="pl-c1">False</span>
<span class="pl-c1">True</span></pre></div>

<h2><a id="user-content-sequential-types-lists-and-tuples" class="anchor" href="#sequential-types-lists-and-tuples" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Sequential types: Lists and Tuples</h2>

<h3><a id="user-content-lists" class="anchor" href="#lists" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Lists</h3>

<p><strong>Lists</strong> are a common data structure to hold an ordered sequence of
elements. Each element can be accessed by an index:</p>

<div class="highlight highlight-source-python"><pre><span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> numbers <span class="pl-k">=</span> [<span class="pl-c1">1</span>,<span class="pl-c1">2</span>,<span class="pl-c1">3</span>]
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> numbers[<span class="pl-c1">0</span>]
<span class="pl-c1">1</span></pre></div>

<p>A <code>for</code> loop can be used to access the elements in a list or other Python data
structure one at a time:</p>

<div class="highlight highlight-source-python"><pre><span class="pl-k">for</span> num <span class="pl-k">in</span> numbers:
    <span class="pl-c1">print</span>(num)
<span class="pl-c1">1</span>
<span class="pl-c1">2</span>
<span class="pl-c1">3</span></pre></div>

<p><strong>Indentation</strong> is very important in Python. Note that the second line in the
example above is indented. This is Python's way of marking a block of code. We will
discuss this in more detail later.</p>

<p>To add elements to the end of a list, we can use the <code>append</code> method:</p>

<div class="highlight highlight-source-python"><pre><span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> numbers.append(<span class="pl-c1">4</span>)
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> <span class="pl-c1">print</span>(numbers)
[<span class="pl-c1">1</span>,<span class="pl-c1">2</span>,<span class="pl-c1">3</span>,<span class="pl-c1">4</span>]</pre></div>

<p>Methods are a way to interact with an object - like a list. We can use or apply 
a method to a variable or element using the dot <code>.</code>. To find out what methods are
 available, we can use the built-in <code>help</code> command:</p>

<div class="highlight highlight-source-python"><pre><span class="pl-c1">help</span>(numbers)

Help on <span class="pl-c1">list</span> <span class="pl-c1">object</span>:

<span class="pl-k">class</span> <span class="pl-c1">list</span>(<span class="pl-c1">object</span>)
 |  <span class="pl-c1">list</span>() -&gt; <span class="pl-en">new</span> <span class="pl-en">empty</span> <span class="pl-c1">list</span>
 |  <span class="pl-c1">list</span>(<span class="pl-e">iterable</span>) -&gt; <span class="pl-en">new</span> <span class="pl-c1">list</span> <span class="pl-en">initialized</span> <span class="pl-k">from</span> <span class="pl-en">iterable</span>'<span class="pl-en">s</span> <span class="pl-en">items</span>
 ...</pre></div>

<p>We can also access a list of methods using <code>dir</code>. Some methods names are
surrounded by double underscores. Those methods are called "special", and
usually we access them in a different way. For example <code>__add__</code> method is
responsible for the <code>+</code> operator.</p>

<div class="highlight highlight-source-python"><pre><span class="pl-c1">dir</span>(numbers)
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> <span class="pl-c1">dir</span>(numbers)
[<span class="pl-s"><span class="pl-pds">'</span>__add__<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>__class__<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>__contains__<span class="pl-pds">'</span></span>, <span class="pl-c1">...</span>]</pre></div>

<h3><a id="user-content-tuples" class="anchor" href="#tuples" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Tuples</h3>

<p>A tuple is similar to a list in that it's an ordered sequence of elements. However,
tuples can not be changed once created (they are "immutable"). Tuples are
created by placing comma-separated values inside parentheses <code>()</code>.</p>

<div class="highlight highlight-source-python"><pre><span class="pl-c"># tuples use paratheses</span>
a_tuple<span class="pl-k">=</span> (<span class="pl-c1">1</span>,<span class="pl-c1">2</span>,<span class="pl-c1">3</span>)
another_tuple <span class="pl-k">=</span> (<span class="pl-s"><span class="pl-pds">'</span>blue<span class="pl-pds">'</span></span>,<span class="pl-s"><span class="pl-pds">'</span>green<span class="pl-pds">'</span></span>,<span class="pl-s"><span class="pl-pds">'</span>red<span class="pl-pds">'</span></span>)
<span class="pl-c"># notes lists uses square brackets</span>
a_list <span class="pl-k">=</span> [<span class="pl-c1">1</span>,<span class="pl-c1">2</span>,<span class="pl-c1">3</span>]</pre></div>

<h3><a id="user-content-challenge" class="anchor" href="#challenge" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Challenge</h3>

<ol>
<li>What happens when you type <code>a_tuple[2]=5</code> vs <code>a_list[1]=5</code> ?</li>
<li>Type <code>type(a_tuple)</code> into python - what is the object type?</li>
</ol>

<h2><a id="user-content-dictionaries" class="anchor" href="#dictionaries" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Dictionaries</h2>

<p>A <strong>dictionary</strong> is a container that holds pairs of objects - keys and values.</p>

<div class="highlight highlight-source-python"><pre><span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> translation <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">"</span>one<span class="pl-pds">"</span></span> : <span class="pl-c1">1</span>, <span class="pl-s"><span class="pl-pds">"</span>two<span class="pl-pds">"</span></span> : <span class="pl-c1">2</span>}
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> translation[<span class="pl-s"><span class="pl-pds">"</span>one<span class="pl-pds">"</span></span>]
<span class="pl-c1">1</span></pre></div>

<p>Dictionaries work a lot like lists - except that you index them with <em>keys</em>. 
You can think about a key as a name for or a unique identifier for a set of values
in the dictionary. Keys can only have particular types - they have to be 
"hashable". Strings and numeric types are acceptable, but lists aren't.</p>

<div class="highlight highlight-source-python"><pre><span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> rev <span class="pl-k">=</span> {<span class="pl-c1">1</span> : <span class="pl-s"><span class="pl-pds">"</span>one<span class="pl-pds">"</span></span>, <span class="pl-c1">2</span> : <span class="pl-s"><span class="pl-pds">"</span>two<span class="pl-pds">"</span></span>}
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> rev[<span class="pl-c1">1</span>]
<span class="pl-s"><span class="pl-pds">'</span>one<span class="pl-pds">'</span></span>
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> bad <span class="pl-k">=</span> {[<span class="pl-c1">1</span>,<span class="pl-c1">2</span>,<span class="pl-c1">3</span>] : <span class="pl-c1">3</span>}
<span class="pl-c1">...</span>
<span class="pl-c1">TypeError</span>: unhashable <span class="pl-c1">type</span>: <span class="pl-s"><span class="pl-pds">'</span>list<span class="pl-pds">'</span></span></pre></div>

<p>To add an item to the dictionary we assign a value to a new key:</p>

<div class="highlight highlight-source-python"><pre><span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> rev <span class="pl-k">=</span> {<span class="pl-c1">1</span> : <span class="pl-s"><span class="pl-pds">"</span>one<span class="pl-pds">"</span></span>, <span class="pl-c1">2</span> : <span class="pl-s"><span class="pl-pds">"</span>two<span class="pl-pds">"</span></span>}
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> rev[<span class="pl-c1">3</span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">"</span>three<span class="pl-pds">"</span></span>
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> rev
{<span class="pl-c1">1</span>: <span class="pl-s"><span class="pl-pds">'</span>one<span class="pl-pds">'</span></span>, <span class="pl-c1">2</span>: <span class="pl-s"><span class="pl-pds">'</span>two<span class="pl-pds">'</span></span>, <span class="pl-c1">3</span>: <span class="pl-s"><span class="pl-pds">'</span>three<span class="pl-pds">'</span></span>}</pre></div>

<p>Using <code>for</code> loops with dictionaries is a little more complicated. We can do this
in two ways:</p>

<div class="highlight highlight-source-python"><pre><span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> <span class="pl-k">for</span> key, value <span class="pl-k">in</span> rev.items():
<span class="pl-c1">...</span>     <span class="pl-c1">print</span>(key, <span class="pl-s"><span class="pl-pds">"</span>-&gt;<span class="pl-pds">"</span></span>, value)
<span class="pl-c1">...</span>
<span class="pl-c1">1</span> <span class="pl-ii">-&gt;</span> one
<span class="pl-c1">2</span> <span class="pl-ii">-&gt;</span> two
<span class="pl-c1">3</span> <span class="pl-ii">-&gt;</span> three</pre></div>

<p>or</p>

<div class="highlight highlight-source-python"><pre><span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span> <span class="pl-k">for</span> key <span class="pl-k">in</span> rev.keys():
<span class="pl-c1">...</span>     <span class="pl-c1">print</span>(key, <span class="pl-s"><span class="pl-pds">"</span>-&gt;<span class="pl-pds">"</span></span>, rev[key])
<span class="pl-c1">...</span>
<span class="pl-c1">1</span> <span class="pl-ii">-&gt;</span> one
<span class="pl-c1">2</span> <span class="pl-ii">-&gt;</span> two
<span class="pl-c1">3</span> <span class="pl-ii">-&gt;</span> three
<span class="pl-k">&gt;&gt;</span><span class="pl-k">&gt;</span></pre></div>

<h3><a id="user-content-challenge-1" class="anchor" href="#challenge-1" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Challenge</h3>

<p>Can you do reassignment in a dictionary? Give it a try. </p>

<ol>
<li><p>First check what <code>rev</code> is right now (remember <code>rev</code> is the name of our dictionary). </p>

<p>Type:
<code>&gt;&gt;&gt; rev</code></p>

<p>You should see the following output:
<code>{1: 'one', 2: 'two', 3: 'three'}</code></p></li>
<li>Try to reassign the second value (in the <em>key value pair</em>) so that it no longer reads "two" but instead reads "apple-sauce". 
<code>&gt;&gt;&gt; rev[2] = "apple-sauce"</code></li>
<li>Now display <code>rev</code> again to see if it has changed; you should see the following:
<code>{1: 'one', 2: 'apple-sauce', 3: 'three'}</code></li>
</ol>

<p>It is important to note that dictionaries are "unordered" and do not remember the
sequence of their items (i.e. the order in which key:value pairs were added to 
the dictionary). Because of this, the order in which items are returned from loops
over dictionaries might appear random and can even change with time.</p>

<h2><a id="user-content-functions" class="anchor" href="#functions" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Functions</h2>

<p>Defining part of a program in Python as a function is done using the <code>def</code>
keyword. For example a function that takes two arguments and returns their sum
can be defined as:</p>

<div class="highlight highlight-source-python"><pre><span class="pl-k">def</span> <span class="pl-en">add_function</span>(<span class="pl-smi">a</span>, <span class="pl-smi">b</span>):
    result <span class="pl-k">=</span> a <span class="pl-k">+</span> b
    <span class="pl-k">return</span> result

z <span class="pl-k">=</span> add_function(<span class="pl-c1">20</span>, <span class="pl-c1">22</span>)
<span class="pl-c1">print</span>(z)
<span class="pl-c1">42</span></pre></div>

<p>Key points here:</p>

<ul>
<li>definition starts with <code>def</code></li>
<li>function body is indented</li>
<li><code>return</code> keyword precedes returned value</li>
</ul>
</article>
  </div>

</div>

<button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="hidden">Jump to Line</button>
<div id="jump-to-line" style="display:none">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>


    </div>
  </div>

    </div>

        <div class="container site-footer-container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage" class="site-footer-mark" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2016 <span title="0.13635s from github-fe158-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



    

    <div id="ajax-error-message" class="ajax-error-message flash flash-error">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"></path></svg>
      <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
        <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
      </button>
      You can't perform that action at this time.
    </div>


      
      <script crossorigin="anonymous" integrity="sha256-79uFEGG7eTPQ5An4vmf2rkg6L6hhK5E64meKpKv0Vpo=" src="https://assets-cdn.github.com/assets/frameworks-efdb851061bb7933d0e409f8be67f6ae483a2fa8612b913ae2678aa4abf4569a.js"></script>
      <script async="async" crossorigin="anonymous" integrity="sha256-jO/U04c/0p2Bc/mzlvwVw1/eIJli+TfHOQcpcftKYsM=" src="https://assets-cdn.github.com/assets/github-8cefd4d3873fd29d8173f9b396fc15c35fde209962f937c739072971fb4a62c3.js"></script>
      
      
      
      
      
      
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner hidden">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"></path></svg>
      <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
      <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
    <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
    </button>
  </div>
</div>

  </body>
</html>

