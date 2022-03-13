CREATE TABLE `daily_jiong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_date` bigint(20) DEFAULT '0' COMMENT '原始文章时间戳',
  `article_type` int(11) DEFAULT '0' COMMENT '0-首篇文章 1-其他文章',
  `title` varchar(255) DEFAULT '',
  `digest` varchar(255) DEFAULT '',
  `cover` varchar(255) DEFAULT '',
  `content_url` varchar(255) DEFAULT '',
  `pic_url` varchar(255) DEFAULT '',
  `pic_type` varchar(10) DEFAULT NULL,
  `pic_size` int(11) DEFAULT NULL,
  `pic_path` varchar(255) DEFAULT '' COMMENT '图片本地存储地址',
  `pic_qiniu_url` varchar(255) DEFAULT '' COMMENT '七牛云地址',
  `emoji_url` varchar(255) DEFAULT '',
  `last_show_time` datetime DEFAULT NULL COMMENT '最近一次图片使用日期',
  `show_count` int(11) DEFAULT '0' COMMENT '展示次数\n',
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='每日一囧';