CREATE TABLE `casosCovid` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `ciudad` varchar(100) NOT NULL,
  `edad` varchar(3) NOT NULL,
  `sexo` varchar(4) NOT NULL,
  `estado` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;