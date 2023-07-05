
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-MBYVRNZK8N');

{"@context":"https://schema.org","@graph":[{"@type":["Person","Organization"],"@id":"https://infocosevi.co.cr/#person","name":"admin","sameAs":["https://twitter.com/mntzjavi_ac2mrfx4"],"logo":{"@type":"ImageObject","@id":"https://infocosevi.co.cr/#logo","url":"https://infocosevi.co.cr/wp-content/uploads/2022/09/cropped-citascosevi-150x90.jpg","contentUrl":"https://infocosevi.co.cr/wp-content/uploads/2022/09/cropped-citascosevi-150x90.jpg","caption":"admin","inLanguage":"es"},"image":{"@type":"ImageObject","@id":"https://infocosevi.co.cr/#logo","url":"https://infocosevi.co.cr/wp-content/uploads/2022/09/cropped-citascosevi-150x90.jpg","contentUrl":"https://infocosevi.co.cr/wp-content/uploads/2022/09/cropped-citascosevi-150x90.jpg","caption":"admin","inLanguage":"es"}},{"@type":"WebSite","@id":"https://infocosevi.co.cr/#website","url":"https://infocosevi.co.cr","name":"admin","publisher":{"@id":"https://infocosevi.co.cr/#person"},"inLanguage":"es","potentialAction":{"@type":"SearchAction","target":"https://infocosevi.co.cr/?s={search_term_string}","query-input":"required name=search_term_string"}},{"@type":"ImageObject","@id":"https://infocosevi.co.cr/wp-content/uploads/2022/06/Citas-Cosevi.jpg","url":"https://infocosevi.co.cr/wp-content/uploads/2022/06/Citas-Cosevi.jpg","width":"390","height":"200","caption":"Citas Cosevi","inLanguage":"es"},{"@type":"WebPage","@id":"https://infocosevi.co.cr/#webpage","url":"https://infocosevi.co.cr/","name":"Citas Cosevi - infocosevi.co.cr","datePublished":"2022-06-23T14:41:25+00:00","dateModified":"2023-05-27T14:37:24+00:00","about":{"@id":"https://infocosevi.co.cr/#person"},"isPartOf":{"@id":"https://infocosevi.co.cr/#website"},"primaryImageOfPage":{"@id":"https://infocosevi.co.cr/wp-content/uploads/2022/06/Citas-Cosevi.jpg"},"inLanguage":"es"},{"@type":"Person","@id":"https://infocosevi.co.cr/author/mntzjavi_ac2mrfx4/","name":"admin","url":"https://infocosevi.co.cr/author/mntzjavi_ac2mrfx4/","image":{"@type":"ImageObject","@id":"https://secure.gravatar.com/avatar/60c7f2160973d82df2a6d4bdda6d9c95?s=96&amp;d=mm&amp;r=g","url":"https://secure.gravatar.com/avatar/60c7f2160973d82df2a6d4bdda6d9c95?s=96&amp;d=mm&amp;r=g","caption":"admin","inLanguage":"es"},"sameAs":["https://infocosevi.co.cr"]},{"@type":"Article","headline":"Citas Cosevi - infocosevi.co.cr","keywords":"Citas cosevi","datePublished":"2022-06-23T14:41:25+00:00","dateModified":"2023-05-27T14:37:24+00:00","author":{"@id":"https://infocosevi.co.cr/author/mntzjavi_ac2mrfx4/","name":"admin"},"publisher":{"@id":"https://infocosevi.co.cr/#person"},"description":"A trav\u00e9s de COSEVI podr\u00e1s pedir citas y obtener o renovar licencias de conducir, placas del veh\u00edculo y muchos otros documentos necesarios para poder transitar","name":"Citas Cosevi - infocosevi.co.cr","@id":"https://infocosevi.co.cr/#richSnippet","isPartOf":{"@id":"https://infocosevi.co.cr/#webpage"},"image":{"@id":"https://infocosevi.co.cr/wp-content/uploads/2022/06/Citas-Cosevi.jpg"},"inLanguage":"es","mainEntityOfPage":{"@id":"https://infocosevi.co.cr/#webpage"}}]}

  $(document).ready(function () {
    $("#myInput").on("keyup", function () {
      var value = $(this).val().toLowerCase();
      $("#myTable tr").filter(function () {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });


  $(document).ready(function () {
    $("#myInput2").on("keyup", function () {
      var value = $(this).val().toLowerCase();
      $("#myTable2 tr").filter(function () {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });


  $(document).ready(function () {
    $("#myInput3").on("keyup", function () {
      var value = $(this).val().toLowerCase();
      $("#myTable3 tr").filter(function () {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });


    <div data-store-id="<%= id %>" class="wpsl-info-window">
		<p>
			<% if ( wpslSettings.storeUrl == 1 && url ) { %>
			<strong><a href="<%= url %>"><%= store %></a></strong>
			<% } else { %>
			<strong><%= store %></strong>
			<% } %>
			<span><%= address %></span>
			<% if ( address2 ) { %>
			<span><%= address2 %></span>
			<% } %>
			<span><%= city %> <%= state %> <%= zip %></span>
		</p>
		<% if ( phone ) { %>
		<span><strong>Teléfono</strong>: <%= formatPhoneNumber( phone ) %></span>
		<% } %>
		<% if ( fax ) { %>
		<span><strong>Fax</strong>: <%= fax %></span>
		<% } %>
		<% if ( email ) { %>
		<span><strong>Email</strong>: <%= formatEmail( email ) %></span>
		<% } %>
		<%= createInfoWindowActions( id ) %>
	</div>


    <li data-store-id="<%= id %>">
		<div class="wpsl-store-location">
			<p><%= thumb %>
				<% if ( wpslSettings.storeUrl == 1 && url ) { %>
				<strong><a href="<%= url %>"><%= store %></a></strong>
				<% } else { %>
				<strong><%= store %></strong>
				<% } %>
				<span class="wpsl-street"><%= address %></span>
				<% if ( address2 ) { %>
				<span class="wpsl-street"><%= address2 %></span>
				<% } %>
				<span><%= city %> <%= state %> <%= zip %></span>
				<span class="wpsl-country"><%= country %></span>
			</p>
			
		</div>
		<div class="wpsl-direction-wrap">
			<%= distance %> km
			<%= createDirectionUrl() %>
		</div>
	</li>


			{
				"@context": "http://schema.org",
				"@type": "WebSite",
				"name": "infocosevi.co.cr",
				"alternateName": "infocosevi.co.cr",
				"url": "https://infocosevi.co.cr"
			}
		


    window.addEventListener("load", function () {

    var cc = initCookieConsent();
    
    function clearCookie(name, domain, path){
	try {
	    function Get_Cookie( check_name ) {
	            // first we'll split this cookie up into name/value pairs
	            // note: document.cookie only returns name=value, not the other components
	            var a_all_cookies = document.cookie.split(';'),
	            	a_temp_cookie = '',
	        		cookie_name = '',
	            	cookie_value = '',
		            b_cookie_found = false;
	    
	            for ( i = 0; i < a_all_cookies.length; i++ ) {
                    // now we'll split apart each name=value pair
                    a_temp_cookie = a_all_cookies[i].split( '=' );
    
                    // and trim left/right whitespace while we're at it
                    cookie_name = a_temp_cookie[0].replace(/^\s+|\s+$/g, '');
    
                    // if the extracted name matches passed check_name
                    if ( cookie_name == check_name ) {
                        b_cookie_found = true;
                        // we need to handle case where cookie has no value but exists (no = sign, that is):
                        if ( a_temp_cookie.length > 1 ) {
                            cookie_value = unescape( a_temp_cookie[1].replace(/^\s+|\s+$/g, '') );
                        }
                        // note that in cases where cookie is initialized but no value, null is returned
                        return cookie_value;
                        break;
                    }
                    a_temp_cookie = null;
                    cookie_name = '';
	            }
	            if ( !b_cookie_found ) {
	              return null;
	            }
	        }
	        if (Get_Cookie(name)) {
                var domain = domain || document.domain;
                var path = path || "/";
                document.cookie = name + "=; expires=" + new Date + "; domain=" + domain + "; path=" + path;
	        }
	}
	catch(err) {}    
};
    
    
    function deleteCookies() {
        var cookies = document.cookie.split(";");

        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i];
            var eqPos = cookie.indexOf("=");
            var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
            if (cookie.indexOf("cc_cookie") == -1) {
                document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;";
                document.cookie = name.trim() + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;";
                clearCookie(name.trim(), window.location.hostname, '/');
                clearCookie(name.trim(), '.'+window.location.hostname, '/');
                clearCookie(name, window.location.hostname, '/');
                clearCookie(name, '.'+window.location.hostname, '/');
            }
        }
    }
    
    function deleteOnlyGaCookies() {
        var cookies = document.cookie.split(";");

        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i];
            var eqPos = cookie.indexOf("=");
            var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
            if (cookie.indexOf("ga") > -1) {
                document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;";
                document.cookie = name.trim() + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;";
                clearCookie(name.trim(), window.location.hostname, '/');
                clearCookie(name.trim(), '.' + window.location.hostname, '/');
                clearCookie(name, window.location.hostname, '/');
                clearCookie(name, '.' + window.location.hostname, '/');
            }
        }
    }
    
    
    
    function addCookies() {
        var script = document.createElement("script");
        script.innerHTML = '';
        document.head.append(script);

        if (cc.allowedCategory('functional')) {
                var script = document.createElement("script");
                    script.innerHTML = '';
            document.head.append(script);
            }

        if (cc.allowedCategory('performance')) {
                var script = document.createElement("script");
                    script.innerHTML = '';
            document.head.append(script);
            }

        if (cc.allowedCategory('analytics_ads')) {
                var script = document.createElement("script");
                    script.innerHTML = '';
            document.head.append(script);
                    var script = document.createElement("script");
                    script.innerHTML = '';
            document.head.append(script);
            }

        if (cc.allowedCategory('other')) {
                var script = document.createElement("script");
                    script.innerHTML = '';
            document.head.append(script);
            }


    }

// run plugin with config object
    cc.run({
    autorun: true,
            delay: 1000,
            current_lang: 'en',
            autoclear_cookies: true,
            cookie_expiration: 365,
            autoload_css: false,
            onAccept: function (cookie) {
                addCookies();
           
                const mediaQuery = window.matchMedia('(max-width: 768px)')
                var hasSocialBottom = document.getElementsByClassName('social-bottom');
                if (mediaQuery.matches && hasSocialBottom.length > 0) {
                    
                   var bottom = hasSocialBottom[0].offsetHeight;
                     document.getElementsByClassName('cc__change_settings')[0].style.bottom = (bottom-1) + "px";
                    
                }
                    document.getElementsByClassName('cc__change_settings')[0].style.visibility = "visible";
                
            },
            onChange: function (cookie) {
               deleteCookies();
               
               addCookies();
                
            },
            languages: {
            'es': {
            consent_modal: {
            title: "",
                    description: 'Esta página web utiliza Cookies con el único fin de mejorar la experiencia de navegación.<a class="c_link link" href="https://infocosevi.co.cr/politica-de-cookies/">Leer más</a>',
                    primary_btn: {
                    text: 'Aceptar',
                            role: 'accept_all'				//'accept_selected' or 'accept_all'
                    },
                    secondary_btn: {
                    text: '',
                            role: 'settings'				//'settings' or 'accept_necessary'
                    }
            },
                    settings_modal: {
                    title: 'Ajustes de Cookies',
                            save_settings_btn: "Guardar Cookies",
                            accept_all_btn: "",
                            cookie_table_headers: [],
                            blocks: [
                            {
                            title: "",
                                    description: 'Esta página web utiliza Cookies con el único fin de mejorar la experiencia de navegación.'
                            },
                            {
                            title: "Strictly necessary cookies",
                                    description: "These cookies are essential to provide you with the services available on our website and to enable you to use some features of our website. Without these cookies, we cannot provide some services on our website.",
                                    toggle: {
                                    value: 'strictly_necessary',
                                            enabled: true,
                                            readonly: true
                                    }
                            },
                                {
                                title: "Functionality Cookies",
                                        description: 'These cookies are used to provide you with a more personalized experience and to remember your choices on our website, for example, we may use functionality cookies to remember your language preferences or your login details.',
                                        toggle: {
                                        value: 'functional',
                                                enabled: false,
                                                readonly: false
                                        }
                                },

                                {
                                title: "Traceability and performance cookies",
                                        description: 'These cookies are used to collect information to analyze traffic and how users use our website. For example, these cookies may collect data such as how long you have been browsing our website or which pages you visit, which helps us to understand how we can improve our website for you. The information collected with these tracking and performance cookies does not identify any individual visitor.',
                                        toggle: {
                                        value: 'performance',
                                                enabled: false,
                                                readonly: false
                                        }
                                },

                                {
                                title: "Tracking and advertising cookies",
                                        description: 'These cookies are used to show you advertisements that may be of interest based on your browsing habits. These cookies, served by our content and/or advertising providers, may combine the information they collected from our website with other information collected by them in connection with your browser activities across their network of websites. If you choose to opt-out or disable tracking and advertising cookies, you will still see advertisements but these may not be of interest to you.',
                                        toggle: {
                                        value: 'analytics_ads',
                                                enabled: false,
                                                readonly: false
                                        }
                                },

                                {
                                title: "Other cookies",
                                        description: 'Other cookies not covered in the previous points.',
                                        toggle: {
                                        value: 'other',
                                                enabled: false,
                                                readonly: false
                                        }
                                },
                            ]
                    }
            }
            }
    });
    cc.show(0);
    
    if (!cc.allowedCategory('analytics_ads')) {
        deleteOnlyGaCookies();
    }
    
    
    });



/* <![CDATA[ */
var wpcf7 = {"api":{"root":"https:\/\/infocosevi.co.cr\/wp-json\/","namespace":"contact-form-7\/v1"}};
/* ]]> */


window.ASL = typeof window.ASL !== 'undefined' ? window.ASL : {}; window.ASL.wp_rocket_exception = "DOMContentLoaded"; window.ASL.ajaxurl = "https:\/\/infocosevi.co.cr\/wp-admin\/admin-ajax.php"; window.ASL.backend_ajaxurl = "https:\/\/infocosevi.co.cr\/wp-admin\/admin-ajax.php"; window.ASL.js_scope = "jQuery"; window.ASL.asl_url = "https:\/\/infocosevi.co.cr\/wp-content\/plugins\/ajax-search-lite\/"; window.ASL.detect_ajax = 1; window.ASL.media_query = 4758; window.ASL.version = 4758; window.ASL.pageHTML = ""; window.ASL.additional_scripts = [{"handle":"wd-asl-ajaxsearchlite","src":"https:\/\/infocosevi.co.cr\/wp-content\/plugins\/ajax-search-lite\/js\/min\/plugin\/optimized\/asl-prereq.js","prereq":[]},{"handle":"wd-asl-ajaxsearchlite-core","src":"https:\/\/infocosevi.co.cr\/wp-content\/plugins\/ajax-search-lite\/js\/min\/plugin\/optimized\/asl-core.js","prereq":[]},{"handle":"wd-asl-ajaxsearchlite-vertical","src":"https:\/\/infocosevi.co.cr\/wp-content\/plugins\/ajax-search-lite\/js\/min\/plugin\/optimized\/asl-results-vertical.js","prereq":["wd-asl-ajaxsearchlite"]},{"handle":"wd-asl-ajaxsearchlite-autocomplete","src":"https:\/\/infocosevi.co.cr\/wp-content\/plugins\/ajax-search-lite\/js\/min\/plugin\/optimized\/asl-autocomplete.js","prereq":["wd-asl-ajaxsearchlite"]},{"handle":"wd-asl-ajaxsearchlite-load","src":"https:\/\/infocosevi.co.cr\/wp-content\/plugins\/ajax-search-lite\/js\/min\/plugin\/optimized\/asl-load.js","prereq":["wd-asl-ajaxsearchlite-autocomplete"]}]; window.ASL.script_async_load = false; window.ASL.init_only_in_viewport = true; window.ASL.font_url = "https:\/\/infocosevi.co.cr\/wp-content\/plugins\/ajax-search-lite\/css\/fonts\/icons2.woff2"; window.ASL.css_async = false; window.ASL.highlight = {"enabled":false,"data":[]}; window.ASL.analytics = {"method":0,"tracking_id":"","string":"?ajax_search={asl_term}","event":{"focus":{"active":1,"action":"focus","category":"ASL","label":"Input focus","value":"1"},"search_start":{"active":0,"action":"search_start","category":"ASL","label":"Phrase: {phrase}","value":"1"},"search_end":{"active":1,"action":"search_end","category":"ASL","label":"{phrase} | {results_count}","value":"1"},"magnifier":{"active":1,"action":"magnifier","category":"ASL","label":"Magnifier clicked","value":"1"},"return":{"active":1,"action":"return","category":"ASL","label":"Return button pressed","value":"1"},"facet_change":{"active":0,"action":"facet_change","category":"ASL","label":"{option_label} | {option_value}","value":"1"},"result_click":{"active":1,"action":"result_click","category":"ASL","label":"{result_title} | {result_url}","value":"1"}}};


/* <![CDATA[ */
var megamenu = {"timeout":"300","interval":"100"};
/* ]]> */


/* <![CDATA[ */
var wpslLabels = {"preloader":"Buscando\u2026","noResults":"No se encontraron resultados","moreInfo":"M\u00e1s informaci\u00f3n","generalError":"Algo sali\u00f3 mal, \u00a1por favor int\u00e9ntalo nuevamente!","queryLimit":"L\u00edmite de uso de API alcanzado","directions":"Direcciones","noDirectionsFound":"No se encontr\u00f3 una ruta entre el origen y el destino","startPoint":"Punto de partida","back":"Regresar","streetView":"Vista de calle","zoomHere":"Hacer zoom aqu\u00ed"};
var wpslGeolocationErrors = {"denied":"Esta aplicaci\u00f3n no tiene permiso para usar el API de Geolocalizaci\u00f3n.","unavailable":"Informaci\u00f3n de ubicaci\u00f3n no disponible.","timeout":"La petici\u00f3n de geolocalizaci\u00f3n agot\u00f3 el tiempo de espera.","generalError":"Ocurri\u00f3 un error desconocido."};
var wpslSettings = {"startMarker":"red@2x.png","markerClusters":"0","streetView":"0","autoComplete":"0","autoLocate":"1","autoLoad":"1","markerEffect":"bounce","markerStreetView":"0","markerZoomTo":"0","newWindow":"0","resetMap":"0","directionRedirect":"0","phoneUrl":"0","clickableDetails":"0","moreInfoLocation":"info window","mouseFocus":"0","templateId":"default","maxResults":"3","searchRadius":"50","distanceUnit":"km","geoLocationTimeout":"7500","ajaxurl":"https:\/\/infocosevi.co.cr\/wp-admin\/admin-ajax.php","mapControls":"<div id=\"wpsl-map-controls\" ><div class=\"wpsl-icon-direction\"><span>\ue800<\/span><\/div><\/div>","storeMarker":"blue@2x.png","mapType":"roadmap","mapTypeControl":"0","zoomLevel":"3","startLatlng":"9.748917,-83.753428","autoZoomLevel":"15","scrollWheel":"1","controlPosition":"left","url":"https:\/\/infocosevi.co.cr\/wp-content\/plugins\/wp-store-locator\/","markerIconProps":{"scaledSize":"24,35","origin":"0,0","anchor":"12,35"},"storeUrl":"0","maxDropdownHeight":"300","enableStyledDropdowns":"1","mapTabAnchor":"wpsl-map-tab","mapTabAnchorReturn":"","gestureHandling":"auto","directionsTravelMode":"DRIVING","runFitBounds":"1","mapStyle":""};
/* ]]> */

