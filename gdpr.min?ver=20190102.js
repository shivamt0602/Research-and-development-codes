(function () {
    function aa() {
        function V(b, a) {
            return b.classList ? b.classList.contains(a) : !!b.className.match(new RegExp("(\\s|^)" + a + "(\\s|$)"));
        }
        function R(b, a) {
            b.classList ? b.classList.remove(a) : (b.className = b.className.replace(new RegExp("(\\s|^)" + a + "(\\s|$)"), " "));
        }
        function A(b, a) {
            b.classList ? b.classList.add(a) : V(b, a) || (b.className += " " + a);
        }
        function H(b) {
            if ("object" === typeof b) {
                var a = [],
                    c = 0;
                for (a[c++] in b);
                return a;
            }
        }
        function w(b, a, c, d, f) {
            d = d || !1;
            var p =
                "number" !== typeof f
                    ? c
                    : function () {
                          c(f);
                      };
            b.addEventListener ? (d ? b.addEventListener(a, p, { passive: !0 }) : b.addEventListener(a, p, !1)) : ("click" == a && (a = "onclick"), b.attachEvent(a, p));
        }
        function I(b) {
            return (b = document.cookie.match("(^|;)\\s*" + b + "\\s*=\\s*([^;]+)")) ? b.pop() : "";
        }
        function W(b, a) {
            for (var c = b.length, d = 0; d < c; d++) if (b[d] == a) return !0;
            return !1;
        }
        function ba(b, a) {
            if (b.autoload_css && !document.getElementById("cc__style")) {
                var c = document.createElement("style");
                c.id = "cc__style";
                var d = new XMLHttpRequest();
                d.onreadystatechange = function () {
                    4 == this.readyState &&
                        200 == this.status &&
                        (c.setAttribute("type", "text/css"),
                        c.styleSheet ? (c.styleSheet.cssText = this.responseText) : c.appendChild(document.createTextNode(this.responseText)),
                        document.getElementsByTagName("head")[0].appendChild(c),
                        setTimeout(function () {
                            a();
                        }, 30));
                };
                d.open("GET", b.theme_css);
                d.send();
            } else a();
        }
        function J(b, a) {
            var c = document.querySelectorAll(".c_toggle"),
                d = "",
                f = !1;
            if ("number" === typeof c.length) {
                switch (a) {
                    case -1:
                        for (a = 0; a < c.length; a++) c[a].checked ? ((d += '"' + c[a].value + '",'), t[a] || ((f = !0), (t[a] = !0))) : t[a] && ((f = !0), (t[a] = !1));
                        break;
                    case 0:
                        for (a = 0; a < c.length; a++) c[a].readOnly ? ((d += '"' + c[a].value + '",'), (t[a] = !0)) : ((c[a].checked = !1), t[a] && ((f = !0), (t[a] = !1)));
                        break;
                    case 1:
                        for (a = 0; a < c.length; a++) (c[a].checked = !0), (d += '"' + c[a].value + '",'), t[a] || (f = !0), (t[a] = !0);
                }
                d = d.slice(0, -1);
                if (b.autoclear_cookies && F) {
                    c = b.languages[u].settings_modal.blocks;
                    a = c.length;
                    for (var p = -1, m = 0; m < a; m++) {
                        var h = c[m];
                        if (h.hasOwnProperty("toggle") && !t[++p] && h.hasOwnProperty("cookie_table"))
                            for (var k = H(b.languages[u].settings_modal.cookie_table_headers[0])[0], l = h.cookie_table.length, C = 0; C < l; C++) {
                                var e = h.cookie_table[C];
                                "" != I(e[k]) &&
                                    ((e = e[k]),
                                    (document.cookie = e + "=; Path=/; Domain=" + location.host + "; Expires=Thu, 01 Jan 1970 00:00:01 GMT;"),
                                    (document.cookie = e + "=; Path=/; Domain=." + location.host + "; Expires=Thu, 01 Jan 1970 00:00:01 GMT;"));
                            }
                    }
                }
            }
            d = '{"level": [' + d + "]}";
            if (!F || f)
                (c = new Date()),
                    c.setTime(c.getTime() + 864e5 * X),
                    (c = "; expires=" + c.toUTCString()),
                    (document.cookie = "https:" === location.protocol ? "cc_cookie=" + (d || "") + c + "; path=/; Domain=" + window.location.host + "; SameSite=Lax; Secure" : "cc_cookie=" + (d || "") + c + "; path=/; SameSite=Lax;");
            if ("function" === typeof b.onAccept && !F) return (F = !0), b.onAccept(JSON.parse(d));
            if ("function" === typeof b.onChange && f) b.onChange(JSON.parse(d));
        }
        function ca(b, a) {
            x = document.createElement("div");
            x.setAttribute("c_data", "c_cookie_main");
            x.style.position = "fixed";
            x.style.zIndex = "1000000";
            x.innerHTML = '\x3c!--[if lt IE 9 ]><div id="cc_div" class="ie"></div><![endif]--\x3e\x3c!--[if (gt IE 8)|!(IE)]>\x3c!--\x3e<div id="cc_div"></div>\x3c!--<![endif]--\x3e';
            var c = x.children[0];
            if (!b) {
                K = document.createElement("div");
                var d = document.createElement("div"),
                    f = document.createElement("p"),
                    p = document.createElement("p"),
                    m = document.createElement("div"),
                    h = document.createElement("button"),
                    k = document.createElement("button");
                K.id = "cm";
                d.id = "cm_inner";
                f.id = "cm_title";
                p.id = "cm_text";
                m.id = "cm_btns";
                h.id = "cm_primary_btn";
                k.id = "cm_secondary_btn";
                h.setAttribute("type", "button");
                h.className = "c_button";
                k.className = "c_link";
                K.style.visibility = "hidden";
                k.setAttribute("type", "button");
                var l = u;
                f.innerHTML = a.languages[l].consent_modal.title;
                p.innerHTML = a.languages[l].consent_modal.description;
                h.innerHTML = a.languages[l].consent_modal.primary_btn.text;
                k.innerHTML = a.languages[l].consent_modal.secondary_btn.text;
                "accept_all" == a.languages[l].consent_modal.primary_btn.role
                    ? w(h, "click", function () {
                          g.hide();
                          J(a, 1);
                      })
                    : w(h, "click", function () {
                          g.hide();
                          J(a, -1);
                      });
                d.appendChild(f);
                d.appendChild(p);
                m.appendChild(h);
                m.appendChild(k);
                d.appendChild(m);
                "accept_necessary" == a.languages[l].consent_modal.secondary_btn.role
                    ? w(k, "click", function () {
                          g.hide();
                          J(a, 0);
                      })
                    : w(k, "click", function () {
                          g.showSettings(0);
                      });
                K.appendChild(d);
                c.appendChild(K);
            }
            L = document.createElement("div");
            d = document.createElement("div");
            f = document.createElement("div");
            p = document.createElement("div");
            m = document.createElement("div");
            h = document.createElement("p");
            k = document.createElement("div");
            l = document.createElement("button");
            var C = document.createElement("div");
            l.setAttribute("type", "button");
            L.id = "cs_cont";
            d.id = "cs_valign";
            p.id = "cs_cont_inner";
            f.id = "cs";
            h.id = "cs_title";
            m.id = "cs_inner";
            k.id = "cs_header";
            C.id = "cs_blocks";
            l.id = "cs_close_btn";
            l.innerHTML = "x";
            l.className = "c_button";
            w(l, "click", function () {
                g.hideSettings();
            });
            var e = a.languages[u].settings_modal.blocks,
                B = e.length;
            h.innerHTML = a.languages[u].settings_modal.title;
            for (var S = 0, M = [], q = 0; q < B; ++q) {
                var N = document.createElement("div"),
                    v = document.createElement("div"),
                    O = document.createElement("div"),
                    r = document.createElement("p"),
                    y = document.createElement("p");
                N.className = "cs_block";
                r.className = "b_title";
                v.className = "cc_title";
                O.className = "desc";
                r.innerHTML = e[q].title;
                y.innerHTML = e[q].description;
                v.appendChild(r);
                if ("undefined" !== typeof e[q].toggle) {
                    r = document.createElement("label");
                    var n = document.createElement("input"),
                        z = document.createElement("span");
                    r.className = "c_b_toggle";
                    n.className = "c_toggle";
                    n.setAttribute("aria-label", "toggle");
                    z.className = "sc_toggle";
                    n.setAttribute("type", "checkbox");
                    n.value = e[q].toggle.value;
                    n.setAttribute("aria-label", e[q].toggle.value);
                    b ? (W(JSON.parse(I("cc_cookie")).level, e[q].toggle.value) ? ((n.checked = !0), t.push(!0)) : t.push(!1)) : e[q].toggle.enabled && (n.checked = !0);
                    e[q].toggle.readonly && ((n.disabled = "disabled"), (n.readOnly = !0), A(z, "sc_readonly"));
                    r.appendChild(n);
                    r.appendChild(z);
                    v.appendChild(r);
                    A(O, "accordion");
                    A(v, "block_button");
                    A(N, "block__expand");
                    M.push(v);
                    w(
                        M[S],
                        "click",
                        function (T) {
                            V(M[T].parentNode, "_active") ? R(M[T].parentNode, "_active") : A(M[T].parentNode, "_active");
                        },
                        !1,
                        S
                    );
                    S++;
                }
                N.appendChild(v);
                O.appendChild(y);
                if ("undefined" !== typeof e[q].cookie_table) {
                    v = document.createElement("table");
                    z = document.createElement("thead");
                    var G = document.createElement("tr");
                    y = a.languages[u].settings_modal.cookie_table_headers;
                    for (var D = 0; D < y.length; ++D) {
                        var E = document.createElement("th");
                        r = H(y[D])[0];
                        n = y[D][r];
                        E.innerHTML = n;
                        G.appendChild(E);
                    }
                    z.appendChild(G);
                    v.appendChild(z);
                    z = document.createElement("tbody");
                    for (G = 0; G < e[q].cookie_table.length; G++) {
                        D = document.createElement("tr");
                        for (E = 0; E < y.length; ++E) {
                            var U = document.createElement("td");
                            r = H(y[E])[0];
                            n = e[q].cookie_table[G][r];
                            U.innerHTML = n;
                            U.setAttribute("data-column", y[E][r]);
                            D.appendChild(U);
                        }
                        z.appendChild(D);
                    }
                    v.appendChild(z);
                    O.appendChild(v);
                }
                N.appendChild(O);
                C.appendChild(N);
            }
            b = document.createElement("div");
            e = document.createElement("button");
            B = document.createElement("button");
            b.id = "cs_buttons";
            e.id = "cs_save__btn";
            B.id = "cs_acceptall_btn";
            e.setAttribute("type", "button");
            B.setAttribute("type", "button");
            e.className = "c_button";
            B.className = "c_button";
            e.innerHTML = a.languages[u].settings_modal.save_settings_btn;
            B.innerHTML = a.languages[u].settings_modal.accept_all_btn;
            b.appendChild(B);
            b.appendChild(e);
            w(e, "click", function () {
                g.hideSettings();
                g.hide();
                J(a, -1);
            });
            w(B, "click", function () {
                g.hideSettings();
                g.hide();
                J(a, 1);
            });
            k.appendChild(h);
            k.appendChild(l);
            m.appendChild(k);
            m.appendChild(C);
            m.appendChild(b);
            p.appendChild(m);
            f.appendChild(p);
            d.appendChild(f);
            L.appendChild(d);
            L.style.visibility = "hidden";
            c.appendChild(L);
            document.body.appendChild(x);
        }
        function Y(b, a) {
            if (a.hasOwnProperty(b)) return b;
            if (0 < H(a).length) return a.hasOwnProperty(u) ? u : H(a)[0];
        }
        function da() {
            for (var b = document.querySelectorAll('a[data-cc="c-settings"], button[data-cc="c-settings"]'), a = 0; a < b.length; a++)
                w(b[a], "click", function (c) {
                    c.preventDefault ? c.preventDefault() : (c.returnValue = !1);
                    g.showSettings(0);
                });
        }
        function ea(b) {
            "number" === typeof b.cookie_expiration && (X = b.cookie_expiration);
            "boolean" === typeof b.autorun && (Z = b.autorun);
            if (b.auto_language) {
                var a = navigator.language || navigator.browserLanguage;
                2 < a.length && (a = a[0] + a[1]);
                u = Y(a.toLowerCase(), b.languages);
            } else "string" === typeof b.current_lang && (u = Y(b.current_lang, b.languages));
        }
        var g = {},
            P = !1,
            F = !1,
            Q = document.documentElement,
            x = null,
            K = null,
            L = null,
            t = [],
            u = "en",
            Z = !0,
            X = 182;
        g.allowedCategory = function (b) {
            return W(JSON.parse(I("cc_cookie") || "{}").level || [], b);
        };
        g.run = function (b) {
            if (!x) {
                ea(b);
                var a = I("cc_cookie");
                P = "" == a;
                ba(b, function () {
                    ca(!P, b);
                    da();
                    setTimeout(function () {
                        A(x, "c--anim");
                    }, 10);
                    !a && Z && g.show(30 < b.delay ? b.delay : 30);
                    a && "function" === typeof b.onAccept && !F && ((F = !0), b.onAccept(JSON.parse(a || "{}")));
                });
            }
        };
        g.showSettings = function (b) {
            setTimeout(
                function () {
                    A(Q, "show--settings");
                },
                0 < b ? b : 0
            );
        };
        g.loadScript = function (b, a, c) {
            if (document.querySelector('script[src="' + b + '"]')) a();
            else {
                var d = document.createElement("script");
                if (c && 0 < c.length) for (var f = 0; f < c.length; ++f) d.setAttribute(c[f].name, c[f].value);
                d.readyState
                    ? (d.onreadystatechange = function () {
                          if ("loaded" === d.readyState || "complete" === d.readyState) (d.onreadystatechange = null), a();
                      })
                    : (d.onload = a);
                d.src = b;
                document.getElementsByTagName("head")[0].appendChild(d);
            }
        };
        g.show = function (b) {
            P &&
                setTimeout(
                    function () {
                        A(Q, "show--consent");
                    },
                    0 < b ? b : 0
                );
        };
        g.hide = function () {
            P && R(Q, "show--consent");
        };
        g.hideSettings = function () {
            R(Q, "show--settings");
        };
        g.validCookie = function (b) {
            return "" != I(b);
        };
        return g;
    }
    "function" !== typeof window.initCookieConsent && (window.initCookieConsent = aa);
})();
