use emprenesy;
INSERT INTO restaurantes (nombreresta, logo, tiporesta, descripresta, paginaresta, menu, horario, horarioApertura,
 horarioCierre, correoresta, telresta, fecha_publicacion, codadmin) 
VALUES ('Cantina La 15', 'galeriaRes/cantinala15.jpg', 'Comida Internacional', 'Cantina La 15 es un lugar vibrante que combina la auténtica cocina mexicana con entretenimiento en vivo. Ofrecen una experiencia gastronómica y artística inolvidable.',
 'https://www.cantinala15.com/', 'https://www.cantinala15.com/menu/', 'Abierto todos los días desde las 6:00 p. m.', '18:00:00', '21:45:00',
 null, ' 300 9133447', '2024-05-15', 2);
 
SELECT LAST_INSERT_ID() INTO @idresta;
 
-- Insertar en redes sociales
INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@idresta, 'restaurante', 'Instagram', 'https://www.instagram.com/cantinala15/?hl=es'),
       (@idresta, 'restaurante', 'TikTok', 'https://www.tiktok.com/@cantinala15co?lang=es');

-- Insertar en galeriaresta
INSERT INTO galeriaresta (idresta, imagenresta, descripcion) 
VALUES (@idresta, 'galeriaRes\\cantina1.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\cantina2.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\cantina3.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\cantina4.jpg', 'Imágen de restaurante');

-- Insertar en ubicacionresta
INSERT INTO ubicacionresta (idresta, ubicacion) 
VALUES (@idresta, 'Carrera 13 #83-57 Bogotá');
#**********************************************************************************************************************
 INSERT INTO restaurantes (nombreresta, logo, tiporesta, descripresta, paginaresta, menu, horario, horarioApertura,
 horarioCierre, correoresta, telresta, fecha_publicacion, codadmin)
VALUES ('Burger King', 'galeriaRes/kingLogo.png', 'Comida rápida', ' Burger King es conocida por servir productos de alta calidad, con hamburguesas 100% hechas a la parrilla y a precios accesibles. Su lema es “The Home of The Whopper” (El hogar de la Whopper)',
 'https://www.burgerking.es/home','https://www.burgerking.es/carta', 'Abierto todos los días', ' 10:00:00 ', '23:00:00',
 null, '300 702 20 00', '2024-05-15', 2);
 
SELECT LAST_INSERT_ID() INTO @idresta;

INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url)
VALUES (@idresta, 'restaurante', 'Instagram', 'https://www.instagram.com/burgerkingcol/?hl=es'),
       (@idresta, 'restaurante', 'TikTok', 'https://www.tiktok.com/@burgerking?lang=es');

INSERT INTO galeriaresta (idresta, imagenresta, descripcion)
VALUES (@idresta, 'galeriaRes\\king1.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\king2.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\king3.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\king4.jpg', 'Imágen de restaurante');

INSERT INTO ubicacionresta (idresta, ubicacion)
VALUES (@idresta, ' Av. Boyacá #19 Bogotá'),
(@idresta, ' Cl. 8 Sur #7184 Bogotá, '),
(@idresta, 'Av. Ferrocarril de Occidente #27-49 LC C 27 Bogotá'),
(@idresta,' Calle 185 #45-03 Bogotá');
#**********************************************************************************************
INSERT INTO restaurantes (nombreresta, logo, tiporesta, descripresta, paginaresta, menu, horario, horarioApertura,
 horarioCierre, correoresta, telresta, fecha_publicacion, codadmin) 
VALUES ('La Kasta Grill and Wine', 'galeriaRes/logoKasta.png', 'Parillas y asaderos', 'La Kasta es un lugar acogedor y de moda en Bogotá, especializado en parrillas y carnes. Ofrecen una variedad de opciones, desde cortes de carne hasta platos con pollo, pescado y mariscos. También cuentan con opciones vegetarianas, vinos, licores y cócteles internacionales',
 'https://linktr.ee/lakasta', 'https://qr.precompro.com/?source=lakasta.precompro.com', 'Lunes a Viernes', '12:00:00', '22:00:00',
 null, '315 4501130', '2024-05-15', 2);
 
SELECT LAST_INSERT_ID() INTO @idresta;

INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@idresta, 'restaurante', 'Instagram', 'https://www.instagram.com/lakasta.dc/'),
       (@idresta, 'restaurante', 'TikTok', 'https://www.tiktok.com/@foodievaro/video/7308477694268689669');

INSERT INTO galeriaresta (idresta, imagenresta, descripcion) 
VALUES (@idresta, 'galeriaRes\\kasta1.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\kasta2.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\kasta3.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\kasta4.jpg', 'Imágen de restaurante');
INSERT INTO ubicacionresta (idresta, ubicacion) 
VALUES (@idresta, 'Calle 40 #21-34, Bogotá'), (@idresta, 'Calle 106 # 18a-41, Bogotá');
#**********************************************************************************************
#**********************************************************************************************************************
INSERT INTO restaurantes (nombreresta, logo, tiporesta, descripresta, paginaresta, menu, horario, horarioApertura,
 horarioCierre, correoresta, telresta, fecha_publicacion, codadmin) 
VALUES ('Frenessí', 'galeriaRes/frenesi.png', 'Comida Internacional', 'Frenessí es un restaurante del Grupo Seratta que ofrece una experiencia gastronómica única. Con solo 16 puestos, te sumergirás en un mundo de realidad virtual mientras disfrutas de un menú experiencial que te llevará a lugares inimaginables.',
 'https://www.frenessi.co/', 'https://www.frenessi.co/service-page/menu-experiencial-above-and-below', 'Abierto todos los días', '18:00:00', '22:30:00',
 null, ' 311 4165534', '2024-05-15', 2);
 
SELECT LAST_INSERT_ID() INTO @idresta;

INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@idresta, 'restaurante', 'Instagram', 'https://www.instagram.com/frenessi.universe/?hl=es'),
       (@idresta, 'restaurante', 'TikTok', null);

INSERT INTO galeriaresta (idresta, imagenresta, descripcion) 
VALUES (@idresta, 'galeriaRes\\frenesi1.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\frenesi2.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\frenesi3.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\frenesi4.jpg', 'Imágen de restaurante');
INSERT INTO ubicacionresta (idresta, ubicacion) 
VALUES (@idresta, 'Autopista Norte No. 114 - 44, Bogotá');


#**********************************************************************************************************************
INSERT INTO restaurantes (nombreresta, logo, tiporesta, descripresta, paginaresta, menu, horario, horarioApertura,
 horarioCierre, correoresta, telresta, fecha_publicacion, codadmin) 
VALUES ('OKA Grill House', 'galeriaRes/okagrilllogo.png', 'Gourmet', 'OKA Grill House es una parrilla al carbón atrevida y contemporánea que rinde homenaje a la tradición culinaria de Colombia. Refleja la versatilidad y el placer de ingredientes locales en preparaciones internacionales. El ambiente es moderno, con una cocina abierta, amplia terraza al aire libre y decoración única inspirada en la naturaleza colombiana y la Leyenda del Dorado',
 'https://www.facebook.com/OkaGrillHouse/', 'https://oka-grill-house.cluvi.co/oka-grill-house/maincategories', 'Abierto todos los días', '06:00:00', '22:00:00',
 null, ' 601 4434438', '2024-05-15', 2);
 
 SELECT LAST_INSERT_ID() INTO @idresta;
 
INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@idresta, 'restaurante', 'Instagram', 'https://www.instagram.com/okagrillhouse/?hl=es'),
       (@idresta, 'restaurante', 'TikTok', 'https://www.tiktok.com/discover/oka-grill-house-buffet-bogota');

INSERT INTO galeriaresta (idresta, imagenresta, descripcion) 
VALUES (@idresta, 'galeriaRes\\oka1.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\oka2.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\oka3.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\oka4.jpg', 'Imágen de restaurante');
INSERT INTO ubicacionresta (idresta, ubicacion) 
VALUES (@idresta, 'Carrera 37 24 29 Hilton Bogotá');

#**********************************************************************************************************************
INSERT INTO restaurantes (nombreresta, logo, tiporesta, descripresta, paginaresta, menu, horario, horarioApertura,
 horarioCierre, correoresta, telresta, fecha_publicacion, codadmin) 
VALUES ('Home Burgers', 'galeriaRes/burgerLogo.png', 'Gourmet', 'Home Burgers trae el concepto de fast casual a Colombia, con hamburguesas clásicas, hechas con ingredientes de la mejor calidad, deliciosas y frescas',
 'https://homeburgers.com/', 'https://homeburgers.com/', 'Abierto todos los días', '11:30:00', '22:00:00',
 null, '1 5554390', '2024-05-15', 2);
 
SELECT LAST_INSERT_ID() INTO @idresta;
INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@idresta, 'restaurante', 'Instagram', 'https://www.instagram.com/homeburgers_/'),
       (@idresta, 'restaurante', 'TikTok', 'https://www.tiktok.com/@homeburgers_');

INSERT INTO galeriaresta (idresta, imagenresta, descripcion) 
VALUES (@idresta, 'galeriaRes\\burger1.jpeg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\burger2.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\burger3.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\burger4.jpg', 'Imágen de restaurante');
       

INSERT INTO ubicacionresta (idresta, ubicacion) 
VALUES (@idresta, 'Carrera 9 81a-19, Chapinero Bogotá'),
(@idresta, 'AV. Boyacá # 145-62 Bogotá'),
(@idresta, 'Cl 140 # 10A-76 Bogotá'),
(@idresta,'Cl 185 # 45-03 Bogotá');

#**********************************************************************************************************************
INSERT INTO restaurantes (nombreresta, logo, tiporesta, descripresta, paginaresta, menu, horario, horarioApertura,
 horarioCierre, correoresta, telresta, fecha_publicacion, codadmin) 
VALUES ('Imagine Restaurante', 'galeriaRes/imagineLogo.png', 'Restaurante temático', 'Ubicado en el sector de Corferias, al lado del Hotel Black Tower Premium Bogotá, Imagine es un restaurante temático inspirado en los Beatles y lo mejor de la época. Ofrecen una carta muy variada de comida internacional y una selección especial de los mejores platos colombianos que hacen honor a nuestra tierra y sus sabores',
 'https://www.blacktowerhotel.com/es/imagine-restaurant.html', 'https://qr.precompro.com/?source=imagine.precompro.com', 'Abierto todos los días', '10:00:00', '22:00:00',
 null, '318 8365751', '2024-05-15', 2);
 
  SELECT LAST_INSERT_ID() INTO @idresta;
INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@idresta, 'restaurante', 'Instagram', 'https://www.instagram.com/imaginerestaurante/'),
       (@idresta, 'restaurante', 'TikTok', 'https://www.tiktok.com/discover/imagine-restaurante-bogot%C3%A1');

INSERT INTO galeriaresta (idresta, imagenresta, descripcion) 
VALUES (@idresta, 'galeriaRes\\imagine1.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\imagine2.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\imagine3.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\imagine4.jpg', 'Imágen de restaurante');
       
INSERT INTO ubicacionresta (idresta, ubicacion) 
VALUES (@idresta, 'Avenida Calle 24 # 43 a 21, Hotel Black Tower Premium Bogotá');

#**********************************************************************************************************************
INSERT INTO restaurantes (nombreresta, logo, tiporesta, descripresta, paginaresta, menu, horario, horarioApertura,
 horarioCierre, correoresta, telresta, fecha_publicacion, codadmin) 
VALUES ('Mirador La Paloma', 'galeriaRes/palomaLogo.png','Restaurante con vista', ' Este restaurante ofrece una vista espectacular de Bogotá y es conocido por su ambiente romántico. Además, cuenta con música en vivo para celebraciones especiales. Los platos son deliciosos y los cócteles están a la altura. Sin duda, un lugar para disfrutar de una experiencia gastronómica única',
 'https://miradorlapaloma.com/', 'https://www.qrcarta.com/restaurant/bogota/mirador-la-paloma/2987/', 'Abierto todos los días', '12:00:00', '03:00:00',
 ' www.miradorlapaloma@hotmail.com', '3144444955', '2024-05-15', 2);
 
  SELECT LAST_INSERT_ID() INTO @idresta;
INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@idresta, 'restaurante', 'Instagram', 'https://www.instagram.com/miradorlapaloma/?hl=es'),
       (@idresta, 'restaurante', 'TikTok', 'https://www.tiktok.com/discover/restaurante-mirador-la-paloma?lang=es');

INSERT INTO galeriaresta (idresta, imagenresta, descripcion)  
VALUES (@idresta, 'galeriaRes\\paloma1.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\paloma2.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\paloma3.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\paloma4.jpg', 'Imágen de restaurante');
       
INSERT INTO ubicacionresta (idresta, ubicacion) 
VALUES (@idresta, 'La Calera Bogotá');

#*****************************************************************************************************************
INSERT INTO restaurantes (nombreresta, logo, tiporesta, descripresta, paginaresta, menu, horario, horarioApertura,
 horarioCierre, correoresta, telresta, fecha_publicacion, codadmin)
VALUES ('La Mar', 'galeriaRes/laMarLogo.png', 'Comida de Mar', ' Un lugar donde celebran y comparten la vida, el mar, la cultura y la amistad a través de la cocina peruana. Juntando frutos del mar, historia y el sentimiento de todo un país, logran ofrecer una exquisita experiencia gastronómica',
 'https://lamarcebicheria.com/es/Bogota', 'https://lamarcebicheria.com/es/Bogota#', 'Abierto todos los días', ' 12:00:00', '24:00:00',
 'lamar@zonak.com.co', '+571 6292177', '2024-05-15', 2);
 
SELECT LAST_INSERT_ID() INTO @idresta;

INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url)
VALUES (@idresta, 'restaurante', 'Instagram', 'https://www.instagram.com/lamarcebicherialima/?hl=es'),
       (@idresta, 'restaurante', 'TikTok', 'https://www.tiktok.com/discover/la-mar-restaurante');

INSERT INTO galeriaresta (idresta, imagenresta, descripcion)
VALUES (@idresta, 'galeriaRes\\laMar1.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\laMar2.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\laMar3.jpg', 'Imágen de restaurante'),
       (@idresta, 'galeriaRes\\laMar4.jpg', 'Imágen de restaurante');
       
INSERT INTO ubicacionresta (idresta, ubicacion)
VALUES (@idresta, 'Calle 119b no.6-01, Usaquén Bogotá'),
(@idresta, ' Cra. 15A No. 120-26 Bogotá');
#**********************************************************************************************************************
INSERT INTO emprendimientos (nombreempre, logo, tipoempre, descripempre, horarioempre, horarioApertura, 
horarioCierre, paginaempre, producempre, correoempre, telempre, fecha_publicacion, codadmin) 
VALUES ('Artesanías de Colombia.', 'galeriaEmprende/artesaniasColombiaLogo.png', 
'Artesanias', 'Artesanías de Colombia es una sociedad anónima que se dedica al comercio al por menor de otros artículos domésticos en establecimientos especializados. Su objetivo es resaltar la riqueza, diversidad y calidad de las artesanías de cada región y etnia del país', 
'Miércoles a viernes: 09:00 - 19:00,Sábado: 09:00 - 19:00,Domingo: 12:00 - 19:00', '09:00:00', '19:00:00', 'https://artesaniasdecolombia.com.co/PortalAC/General/template_index.jsf',
 'https://artesaniasdecolombia.com.co/PortalAC/Catalogo/CatalogoIndex.jsf', 
 'soytransparente@artesaniasdecolombia.com.co', '305 772 7539', '2024-05-15', 2);

 SELECT LAST_INSERT_ID() INTO @idempre;
INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@idempre, 'emprendimiento', 'Instagram', 'https://www.instagram.com/explore/locations/358810988/artesanias-de-colombia-pagina-oficial/?hl=es'),
       (@idempre, 'emprendimiento', 'TikTok', null);
       
INSERT INTO galeriaempre (idempre, imagenempre, descripcion) 
VALUES (@idempre, 'galeriaEmprende\\artesaniasColombia1.jpg', 'Imagen del emprendimiento'),
       (@idempre, 'galeriaEmprende\\artesaniasColombia2.jpg', 'Imagen del emprendimiento'),
       (@idempre, 'galeriaEmprende\\artesaniasColombia3.jpg', 'Imagen del emprendimiento'),
       (@idempre, 'galeriaEmprende\\artesaniasColombia4.jpg', 'Imagen del emprendimiento');


INSERT INTO ubicacionempre (idempre, ubicacion) 
VALUES (@idempre, 'Calle 74 No. 11-91 Bogotá'),(@idempre, 'Carrera 11 No. 84 - 12 Bogotá');

#**********************************************************************************************************************
INSERT INTO emprendimientos (nombreempre, logo, tipoempre, descripempre, horarioempre, horarioApertura, 
horarioCierre, paginaempre, producempre, correoempre, telempre, fecha_publicacion, codadmin) 
VALUES ('Amorella', 'galeriaEmprende/amorellaLogo.png', 'Tienda de Ropa', 'Amorella es una tienda multimarca colombiana que se destaca por ofrecer una variedad de marcas locales y diseños exclusivos en lencería y ropa interior femenina.', 
'Lunes a Sábado: 10 am - 7 pm, Domingos y festivos: 11:30 am - 6 pm', '10:00:00', '19:00:00', 'https://www.amorellashop.com/',
 'https://www.threads.net/%40amorella.tmm', 'uncorreo@gmail.com', '321546684', '2024-05-15', 2);

 SELECT LAST_INSERT_ID() INTO @idempre;
 
INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@idempre, 'emprendimiento', 'Instagram', 'https://www.instagram.com/amorella.tmm/?hl=es'),
       (@idempre, 'emprendimiento', 'TikTok', 'https://www.tiktok.com/@amorellatmm');
       
INSERT INTO galeriaempre (idempre, imagenempre, descripcion) 
VALUES (@idempre, 'galeriaEmprende\\amorella1.png', 'Imagen del emprendimiento'),
       (@idempre, 'galeriaEmprende\\amorella2.png', 'Imagen del emprendimiento'),
       (@idempre, 'galeriaEmprende\\amorella3.png', 'Imagen del emprendimiento'),
       (@idempre, 'galeriaEmprende\\amorella4.png', 'Imagen del emprendimiento');

INSERT INTO ubicacionempre (idempre, ubicacion) 
VALUES (@idempre, 'Carrera 14 # 79 - 62 Bogotá');

#**********************************************************************************************************************
INSERT INTO emprendimientos (nombreempre, logo, tipoempre, descripempre, horarioempre, horarioApertura, 
horarioCierre, paginaempre, producempre, correoempre, telempre, fecha_publicacion, codadmin) 
VALUES ('La galeria online', 'galeriaEmprende/galeriaLogo.png', 'Emprendimientos de Arte', 'Lagaleriaonline.co es una plataforma de difusión y venta de obras de arte de artistas modernos y contemporáneos, ya establecidos o emergentes, pensado para todos los presupuestos. Nuestro objetivo es intermediar en la conexión de artistas y compradores, a través de nuestra comunidad virtual abierta 24/7 y nuestra sala expositiva Artespacio. Encuentra fotografías, esculturas, dibujos, pinturas, obras gráficas y demás que abarcan todos los estilos y movimientos artísticos. ', 
'Lunes a Sábado: 10 am - 7 pm', '10:00:00', '19:00:00', 'https://lagaleriaonline.co/collections/obras',
 'https://lagaleriaonline.co/collections', 'contacto@lagaleriaonline.co', '314 3371659', '2024-05-15', 2);

 SELECT LAST_INSERT_ID() INTO @idempre;
 
INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@idempre, 'emprendimiento', 'Instagram', 'https://www.instagram.com/lagaleriaonline.co/'),
       (@idempre, 'emprendimiento', 'TikTok', null);
       
INSERT INTO galeriaempre (idempre, imagenempre, descripcion) 
VALUES (@idempre, 'galeriaEmprende\\galeria1.png', 'Imagen del emprendimiento'),
       (@idempre, 'galeriaEmprende\\galeria2.png', 'Imagen del emprendimiento'),
       (@idempre, 'galeriaEmprende\\galeria3.png', 'Imagen del emprendimiento'),
       (@idempre, 'galeriaEmprende\\galeria4.png', 'Imagen del emprendimiento');

INSERT INTO ubicacionempre (idempre, ubicacion) 
VALUES (@idempre, 'Calle 75 # 5 - 88 Bogotá');

#**********************************************************************************************************************
INSERT INTO emprendimientos (nombreempre, logo, tipoempre, descripempre, horarioempre, horarioApertura, 
horarioCierre, paginaempre, producempre, correoempre, telempre, fecha_publicacion, codadmin) 
VALUES ('La Tienda Pet Col', 'galeriaEmprende/petcolLogo.png', 'Emprendimiento de Mascotas', 'La Tienda Pet Col es una tienda de mascotas ubicada en varias partes en Colombia, que se destaca por ofrecer una amplia variedad de productos y servicios para el cuidado y bienestar de mascotas. Con 32 años de experiencia, se enfocan en brindar acompañamiento continuo a los propietarios de mascotas, ofreciendo servicios de excelente calidad y una gran variedad de productos. Desde accesorios, alimentos y juguetes hasta servicios de peluquería y certificados de salud, La Tienda Pet Col se esfuerza por satisfacer las necesidades de las mascotas y sus dueños, entregando productos a domicilio y brindando opciones de pago seguras. ', 
'Lunes a Sábado: 08 am - 6 pm y Domingos: 09 am - 6 pm', '08:00:00', '18:00:00', 'https://petcol.co/',
 'https://petcol.co/collections/all', null , '601 7439999', '2024-05-15', 2);

 SELECT LAST_INSERT_ID() INTO @idempre;
 
INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@idempre, 'emprendimiento', 'Instagram', 'https://www.instagram.com/petcol/?hl=es-la'),
       (@idempre, 'emprendimiento', 'TikTok', 'https://www.tiktok.com/@petcol.oficial?_d=secCgwIARCbDRjEFSACKAESPgo8l7eoQFgMw%2BX6Yw4IPNtXHJqyRbGsbngt2%2Bvo7nM5AoqUEntE4bzxkVo1iWeOurXzNTv0gEgcdQEgGC1kGgA%3D&language=es&sec_uid=MS4wLjABAAAAipX9kLcpDelZ3KbzFPdj4oorppcfWM9gafp0bg_h3m0z_qffBK8UGewLtRGoB7xy&sec_user_id=MS4wLjABAAAAgK9LWZZ597Ipl-um7mBvwXyXT4O_tsk4GYO7tJbWMjUsiT_2hqnOqMv1SnpgC07s&share_app_id=1233&share_author_id=7001196810346120198&share_link_id=4c8190cf-8e4e-46cb-a07e-906b9ca166a1&timestamp=1635202596&u_code=dbe910i4i98bgi&user_id=6807247612288156678&utm_campaign=client_share&utm_medium=android&utm_source=copy&source=h5_m&_r=1');
       
INSERT INTO galeriaempre (idempre, imagenempre, descripcion) 
VALUES (@idempre, 'galeriaEmprende\\petcol1.png', 'Imagen del emprendimiento'),
       (@idempre, 'galeriaEmprende\\petcol2.png', 'Imagen del emprendimiento'),
       (@idempre, 'galeriaEmprende\\petcol3.png', 'Imagen del emprendimiento'),
       (@idempre, 'galeriaEmprende\\petcol4.png', 'Imagen del emprendimiento');

INSERT INTO ubicacionempre (idempre, ubicacion) 
VALUES (@idempre, 'Calle 140 # 13-18 Bogotá'),
(@idempre, 'Carrera 58 # 131A-26 Bogotá'),(@idempre, 'Av Boyacá # 99-76 Bogotá'),
(@idempre, 'Cra 45A #124-5 Bogotá'),(@idempre, 'Calle 70A #4-78 Bogotá');

#**********************************************************************************************************************
INSERT INTO emprendimientos (nombreempre, logo, tipoempre, descripempre, horarioempre, horarioApertura, 
horarioCierre, paginaempre, producempre, correoempre, telempre, fecha_publicacion, codadmin) 
VALUES ('Frutas y Fresas', 'galeriaEmprende/fresasLogo.jpg', 'Emprendimiento Gastronómico', 'Arreglos frutales en Bogotá y fresas con chocolate en Bogotá. Por qué regalar otra cosa cuando puedes regalar algo bonito, creativo y saludable? Nada mejor que expresar lo que sentimos con un saludable y delicioso arreglo frutal  o arreglos de frutas frescas combinadas con unas deliciosas fresas con chocolate. Para los arreglos frutales puedes elegir entre varias opciones de diseño y cantidad de frutas. Al igual que nuestros arreglos de fresas con chocolate. Nuestros arreglos de fruta o fresas cuentan con un delicado proceso de selección. Regalemos a los que más queremos obsequios saludables, arreglos frutales y fresas con chocolate. ', 
'Lunes a Sábado: 08 am - 6 pm ', '08:00:00', '18:00:00', 'https://www.frutasyfresas.com/',
 'https://www.frutasyfresas.com/25-fresas-con-chocolate', 'ventas@frutasyfresas' ,
 '3124479342 ', '2024-05-15', 2);

 SELECT LAST_INSERT_ID() INTO @idempre;
 
INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@idempre, 'emprendimiento', 'Instagram', 'https://www.instagram.com/frutasyfresas.daristizabal/'),
       (@idempre, 'emprendimiento', 'TikTok', null);
       
INSERT INTO galeriaempre (idempre, imagenempre, descripcion) 
VALUES (@idempre, 'galeriaEmprende\\fresas1.png', 'Imagen del emprendimiento'),
       (@idempre, 'galeriaEmprende\\fresas2.png', 'Imagen del emprendimiento'),
       (@idempre, 'galeriaEmprende\\fresas3.png', 'Imagen del emprendimiento'),
       (@idempre, 'galeriaEmprende\\fresas4.png', 'Imagen del emprendimiento');

INSERT INTO ubicacionempre (idempre, ubicacion) 
VALUES (@idempre, 'Calle 140 # 13-18 Bogotá'),
(@idempre, 'Carrera 58 # 131A-26 Bogotá'),(@idempre, 'Av Boyacá # 99-76 Bogotá'),
(@idempre, 'Cra 45A #124-5 Bogotá'),(@idempre, 'Calle 70A #4-78 Bogotá');


#**********************************************************************************************************************
INSERT INTO eventos ( nombreeven, logo, tipoevento, descripeven, paginaeven, boletaseven , 
infoAdicional, contacto , correoeven, fecha_publicacion,codadmin) 
VALUES ('Fesbo','galeriaEventos/fesboLogo.jpg','Evento de danza','Fesbo nace a partir del sueño del maestro Jaime Otáora, director de Bogotá Capital Dance, de congregar y reunir a distintas escuelas de danza de Bogotá con el fin de visibilizar su trabajo en ballet, ballet contemporáneo y/o neoclásico para compartirlo en escena.Se trata de un momento de celebración donde diferentes escuelas de la ciudad: La Coartada, Bogotá Capital Dance y BCD Dance Company se reúnen a celebrar su oficio brindando un espectáculo de primer nivel.',
'https://www.atrapalo.com.co/entradas/fesbo-uniendo-historias-festival-escuelas-bogota_e4909886/','https://www.atrapalo.com.co/entradas/fesbo-uniendo-historias-festival-escuelas-bogota_e4909886/',
'Atrápalo S.A.S. actúa como operador oficial de boletería para este evento y como único canal de venta.
 Atrápalo Colombia S.A.S. no garantizará ni responderá de ninguna forma, por entradas adquiridas en canales diferentes a atrapalo.com.co
 Si compras varias entradas al mismo tiempo, llegarán todas al correo del comprador. Si asistes con otras personas y no van a llegar al mismo tiempo al sitio del evento, puedes imprimirlas, o deberás reenviarlas a sus correos electrónicos para que ellos las presenten al ingreso. Cada entrada tiene un número único de ticket, así que debes asegurarte de asignar una diferente para cada acompañante.',
'312-228-8492','info@atrapalo.com.co','2024-05-15',2);

 SELECT LAST_INSERT_ID() INTO @ideven;
 
INSERT INTO fechaseven (ideven,fechaseven,horarioEntrada,horarioSalida)
VALUES (@ideven,'2024-06-12','19:00:00','21:00:00');

INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@ideven, 'evento', 'Instagram', 'https://www.instagram.com/fesbo_idb/'),
       (@ideven, 'evento', 'TikTok', null);
       
INSERT INTO galeriaeven (ideven ,urlImagen, descripcion) 
VALUES (@ideven, 'galeriaEventos\\fesbo1.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\fesbo2.jpg', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\fesbo3.jpg', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\fesbo4.jpg', 'Imagen del  evento');

INSERT INTO ubicacioneven (ideven, ubicacion) 
VALUES (@ideven, 'Cra. 11 #61-80 Bogotá ');


#**********************************************************************************************************************
INSERT INTO eventos ( nombreeven, logo, tipoevento, descripeven, paginaeven, boletaseven , 
infoAdicional, contacto , correoeven, fecha_publicacion,codadmin) 
VALUES ('Art','galeriaEventos/artLogo.jpg','Eventos de teatro','¡Regresa ART!, la aclamada comedia considerada la mejor de todos los tiempos, regresa tras el rotundo éxito de su primera temporada. Los espectadores disfrutaron de una puesta en escena impecable y divertida, con talentosos actores. Escrita por Yasmina Reza y adaptada en todo el mundo, la obra presenta la amistad de tres hombres desde una perspectiva única. Bajo la dirección de Manuel Orjuela y con las destacadas actuaciones de Diego Trujillo, Emmanuel Esparza y John Alex Toro, la producción de Mariano Bacaleinik llega a Casa E.',
'https://www.atrapalo.com.co/entradas/art_e4909973/','https://www.atrapalo.com.co/entradas/art_e4909973/',
'La trama gira en torno a un aparentemente trivial conflicto que desencadena una profunda crisis en los valores e intereses de los amigos, relacionados con el mercado, la vanguardia, la modernidad y el valor de las cosas según su precio. Las exageradas discusiones generan situaciones hilarantes y risas contagiosas. La pregunta es si esta amistad llegará a su fin o si será un nuevo comienzo.
¡No te pierdas esta imperdible comedia que promete emociones y diversión!
Artistas: Diego Trujillo, John Alex Toro, Emmanuel Esparza',
'312-228-8492','info@atrapalo.com.co','2024-05-15',2);

SELECT LAST_INSERT_ID() INTO @ideven;

INSERT INTO fechaseven (ideven,fechaseven,horarioEntrada,horarioSalida)
VALUES (@ideven,'2024-06-01','18:00:00','19:00:00');

INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@ideven, 'evento', 'Instagram', 'https://www.instagram.com/casaeborrero/p/C6htb96N08x/'),
       (@ideven, 'evento', 'TikTok', null);
       
INSERT INTO galeriaeven (ideven ,urlImagen, descripcion) 
VALUES (@ideven, 'galeriaEventos\\Art1.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\Art2.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\Art3.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\Art4.jpg', 'Imagen del  evento');

INSERT INTO ubicacioneven (ideven, ubicacion) 
VALUES (@ideven, 'Carrera 24 # 41-69 Bogotá ');

#**********************************************************************************************************************
INSERT INTO eventos ( nombreeven, logo, tipoevento, descripeven, paginaeven, boletaseven , 
infoAdicional, contacto , correoeven, fecha_publicacion,codadmin) 
VALUES ('Alimentarte Food Festival','galeriaEventos/alimentarteLogo.png','Ferias gastronomicas','Es el evento gastronómico más destacado de la ciudad de Bogotá. Organizado por la Fundación Corazón Verde, una entidad sin ánimo de lucro reconocida por su compromiso social y por promover la diversidad gastronómica. Durante el festival, cerca de 200 restaurantes de la ciudad trasladan su oferta gastronómica al Parque El Country durante dos fines de semana',
'https://fundacioncorazonverde.org/alimentarte/alimentarte-food-festival/','https://fundacioncorazonverde.org/alimentarte/alimentarte-food-festival/',
'Durante los dos fines de semana del evento, también podrás disfrutar de una muestra de 40 emprendimientos locales en los sectores de moda, joyería, accesorios para mascotas, marroquinería, artesanías y alimentos preparados, gracias a la estrategia Hecho en Bogotá. Las entradas tienen un costo de $11.000 pesos y estarán disponibles en Atrapalo o en las taquillas que estarán disponibles en el parque',
'317-667-0090',null,'2024-05-15',2);

 SELECT LAST_INSERT_ID() INTO @ideven;

INSERT INTO fechaseven (ideven,fechaseven,horarioEntrada,horarioSalida)
VALUES (@ideven,'2024-03-09','11:00:00','22:00:00');

INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@ideven, 'evento', 'Instagram', 'https://www.instagram.com/alimentartefcv/?hl=es-la'),
       (@ideven, 'evento', 'TikTok', 'https://www.tiktok.com/search?lang=es&q=alimentarte%20food%20festival%202024&t=1717589547969');
       
INSERT INTO galeriaeven (ideven ,urlImagen, descripcion) 
VALUES (@ideven, 'galeriaEventos\\alimentarte1.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\alimentarte2.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\alimentarte3.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\alimentarte4.png', 'Imagen del  evento');

INSERT INTO ubicacioneven (ideven, ubicacion) 
VALUES (@ideven, 'Calle 127 #11D-90 Bogotá ');


#**********************************************************************************************************************
INSERT INTO eventos ( nombreeven, logo, tipoevento, descripeven, paginaeven, boletaseven , 
infoAdicional, contacto , correoeven, fecha_publicacion,codadmin) 
VALUES ('Feria Internacional del Libro Bogotá, FILBO','galeriaEventos/feriaLibroLogo.jpg','Ferias de libros','En la Feria Internacional del Libro de Bogotá se reúnen desde hace 35 años, todos los actores de la cadena del libro (autores, editores, correctores, traductores, distribuidores, agentes y libreros) quienes junto con sus lectores conforman este ecosistema del libro que cada año crece y se fortalece, gracias a estos espacios de formación y promoción del libro y la lectura.',
'https://feriadellibro.com/','https://www.facebook.com/FILBogota/',
'Colombia es un país que cuenta con una red de 23 ferias del libro en todo el territorio.  Desde el 2016, la Cámara Colombiana del Libro, con el reconocimiento del Ministerio de Cultura, ha concentrado esfuerzos para reunir a los líderes de las principales ferias del libro del país.',
null,'serviciocliente@corferias.com','2024-05-15',2);

 SELECT LAST_INSERT_ID() INTO @ideven;

INSERT INTO fechaseven (ideven,fechaseven,horarioEntrada,horarioSalida)
VALUES (@ideven,'2024-05-02','09:00:00','20:00:00');

INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@ideven, 'evento', 'Instagram', 'https://www.instagram.com/corferias/'),
       (@ideven, 'evento', 'TikTok', 'https://www.tiktok.com/@corferias');
       
INSERT INTO galeriaeven (ideven ,urlImagen, descripcion) 
VALUES (@ideven, 'galeriaEventos\\feriaLibro1.jpg', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\feriaLibro2.jpg', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\feriaLibro3.jpg', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\feriaLibro4.jpg', 'Imagen del  evento');

INSERT INTO ubicacioneven (ideven, ubicacion) 
VALUES (@ideven, 'Cra 37 # 24 - 67 Bogotá ');


#**********************************************************************************************************************
INSERT INTO eventos ( nombreeven, logo, tipoevento, descripeven, paginaeven, boletaseven , 
infoAdicional, contacto , correoeven, fecha_publicacion,codadmin) 
VALUES ('Nociones de lo Posible','galeriaEventos/arteLogo.jpg','Exposiciones de arte','En "Nociones de lo Posible", la fotografía toma estos rasgos para abordar los diferentes lenguajes que la atraviesan. A partir de una perspectiva documental, artística y experimental, esta exposición plantea un recorrido por diversas manifestaciones desde las cuales se da cuenta de procesos históricos, políticos, sociales y plásticos en Colombia y otros contextos.',
'https://www.arteinformado.com/agenda/f/nociones-de-lo-posible-230768','Entrada gratuita',
'Artistas: Jaime Ardila, Carlos Caicedo, Fernando Cano, Antonio Castles, Hernán Díaz, François Dolmetsch, Alfred Eisenstaedt, Abdu Elajiek, Ida Esbra, Fernell Franco, Umberto Giangrandi, Francisca Jiménez, Camilo Lleras, Danny Lyon, Óscar Monsalve, Helmut Newton, Andrés F. Orjuela, Jorge Ortiz, Federico Pardo, Fernando Pareja, Alejandra Parra, Man Ray, Andrés Sierra, Alfonso Suárez, Sergio Trujillo Dávila, Becky Mayer, Fernando Urbina, Leo Matíz y Manu Mojito.',
null,null,'2024-05-15',2);

 SELECT LAST_INSERT_ID() INTO @ideven;

INSERT INTO fechaseven (ideven,fechaseven,horarioEntrada,horarioSalida)
VALUES (@ideven,'2024-06-01','11:00:00','16:00:00');

INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@ideven, 'evento', 'Instagram', 'https://www.instagram.com/arteinformado/'),
       (@ideven, 'evento', 'TikTok', null);
       
INSERT INTO galeriaeven (ideven ,urlImagen, descripcion) 
VALUES (@ideven, 'galeriaEventos\\arte1.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\arte2.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\arte3.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\arteLogo.jpg', 'Imagen del  evento');

INSERT INTO ubicacioneven (ideven, ubicacion) 
VALUES (@ideven, ' Carrera 4A #26C-37 Bogotá ');

#**********************************************************************************************
INSERT INTO eventos ( nombreeven, logo, tipoevento, descripeven, paginaeven, boletaseven , 
infoAdicional, contacto , correoeven, fecha_publicacion,codadmin) 
VALUES ('WEBCONGRESS LATAM','galeriaEventos/logoWebcongress.png','Ferias tecnológicas','WebCongress es el evento líder en marketing digital, innovación y nuevas tecnologías en el mundo. La Edición #12 en Colombia se llevará a cabo los días 8 y 9 de agosto de 2024 en Bogotá. El tema central es “AI EVERYWHERE: La Inteligencia Artificial está impactando tu realidad”.El evento ofrece conferencias internacionales, networking, expo interactiva y talleres para desarrollar habilidades',
'https://www.webcongress.com/latam','https://welcu.com/webcongress-inc/webcongress-latam-2024',
'Conecta con cientos de tomadores de decisión en la industria tecnológica.Lanzamiento del libro “A.I Everywhere: La Inteligencia Artificial es el nuevo oxígeno de los Negocios” por @Ouali.Sesiones prácticas con expertos en temas como transformación digital, publicidad, estrategia de marketing, emprendimiento, ciencia de datos y más.',
null,'info@webcongress.com','2024-05-15',2);

 SELECT LAST_INSERT_ID() INTO @ideven;

INSERT INTO fechaseven (ideven,fechaseven,horarioEntrada,horarioSalida)
VALUES (@ideven,'2024-08-08','09:00:00','18:00:00');

INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@ideven, 'evento', 'Instagram', 'https://www.instagram.com/webcongress'),
       (@ideven, 'evento', 'TikTok', null);
       
INSERT INTO galeriaeven (ideven ,urlImagen, descripcion) 
VALUES (@ideven, 'galeriaEventos\\webcongress1.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\webcongress2.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\webcongress3.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\webcongress4.png', 'Imagen del  evento');

INSERT INTO ubicacioneven (ideven, ubicacion) 
VALUES (@ideven, 'Cra. 47 ##91-38 La Castellana Bogotá ');

#**********************************************************************************************
INSERT INTO eventos ( nombreeven, logo, tipoevento, descripeven, paginaeven, boletaseven , 
infoAdicional, contacto , correoeven, fecha_publicacion,codadmin) 
VALUES ('Media maratón de Bogotá','galeriaEventos/logoMaraton.png','Eventos deportivos','Este próximo domingo 28 de julio llega uno de los eventos más esperados del año, la Media Maratón de Bogotá (MMB) 2024, la cual continúa posicionando a la capital colombiana como epicentro de la cultura y la recreación, ya que se trata de una de las carreras más importantes y con más acogida en Sudamérica',
'https://www.mediamaratonbogota.com/2024/index.php','https://www.mediamaratonbogota.com/2024/app/runner/login',
'Los filtros para acceder al carril de salida, ubicado sobre la Carrera 60, se habilitarán una hora antes de cada largada. Para la carrera de 21K, esto será a las 7:30 a.m. Las vías por donde circulará la media maratón de Bogotá estarán disponibles para los atletas en los siguientes horarios: de 8:30 a.m. a 1:00 p.m. Se recomienda a los atletas realizar el recorrido dentro de los tiempos establecidos para garantizar una experiencia segura y organizada.',
'601 2563765','info@correcaminoscolombia.com','2024-05-15',2);

 SELECT LAST_INSERT_ID() INTO @ideven;

INSERT INTO fechaseven (ideven,fechaseven,horarioEntrada,horarioSalida)
VALUES (@ideven,'2024-07-28','08:30:00','18:00:00');

INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@ideven, 'evento', 'Instagram', 'https://www.instagram.com/mmboficial'),
       (@ideven, 'evento', 'TikTok', null);
       
INSERT INTO galeriaeven (ideven ,urlImagen, descripcion) 
VALUES (@ideven, 'galeriaEventos\\maraton1.jpg', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\maraton2.jpg', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\maraton3.jpg', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\maraton4.png', 'Imagen del  evento');

INSERT INTO ubicacioneven (ideven, ubicacion) 
VALUES (@ideven, 'parque simon bolivar bogotá');


#**********************************************************************************************
INSERT INTO eventos ( nombreeven, logo, tipoevento, descripeven, paginaeven, boletaseven , 
infoAdicional, contacto , correoeven, fecha_publicacion,codadmin) 
VALUES ('Festival Cordillera','galeriaEventos/logoFestival.png','Conciertos de música','El Parque Simón Bolívar volverá a recibir el sol de septiembre con el sello de los sonidos latinoamericanos en toda su magnitud global. Vuelve el Festival Cordillera para celebrar su tercera edición el 14 y 15 de septiembre de 2024 en el corazón geográfico de Bogotá. Este año le cantaremos a los paisajes más impresionantes que el ojo haya visto, al cariño inmenso de la abuela, a los panas, los parceros, los manitos, los cuates, los pibes y las pibas.',
'https://www.eticket.co/masinformacion.aspx?idevento=14672','https://www.eticket.co/masinformacion.aspx?idevento=14672',
'Artistas confirmados: La alineación incluye a Juan Luis Guerra, Hombres G, Fito Páez, Molotov, Babasónicos, León Larregui, Trueno, Bersuit Vergarabat, Bacilos, Maldita Vecindad, y muchos más.',
'350 3100460','ayuda.eticket.com.co','2024-05-15',2);

 SELECT LAST_INSERT_ID() INTO @ideven;

INSERT INTO fechaseven (ideven,fechaseven,horarioEntrada,horarioSalida)
VALUES (@ideven,'2024-09-14','18:00:00','02:00:00');

INSERT INTO redes_sociales (entidad_id, entidad_tipo, red, url) 
VALUES (@ideven, 'evento', 'Instagram', 'https://www.instagram.com/cordillerafestival/?hl=es'),
       (@ideven, 'evento', 'TikTok', 'https://www.tiktok.com/tag/festivalcordillera');
       
INSERT INTO galeriaeven (ideven ,urlImagen, descripcion) 
VALUES (@ideven, 'galeriaEventos\\cordillera1.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\cordillera2.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\cordillera3.png', 'Imagen del evento'),
       (@ideven, 'galeriaEventos\\cordillera4.png', 'Imagen del  evento');

INSERT INTO ubicacioneven (ideven, ubicacion) 
VALUES (@ideven, 'Carrera 13 A 98 75 Bogotá');
