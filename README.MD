# Каталог `erp_25`

Каталог **erp_25** содержит материалы оценки и проработки функциональных требований по контуру снабжения и обеспечения в проекте на базе **1С:ERP Управление предприятием** (версия 2.5 и смежный контекст).

Здесь собраны текстовые отчёты по требованиям с номерами **10–64**: ведение НСИ, аналоги, заявки и планы потребности, план и программа закупок, лоты и тендеры, ценообразование, заказы поставщикам, склад и перемещения, СИЗ, учёт прослеживаемости (РНПТ), отчёты и интеграции с внешними системами.

**Единица оценки:** все трудозатраты в сводных таблицах и отчётах указаны в **человеко-днях** (чел.-дни) — это оценка объёма работ одного специалиста за один рабочий день. В [total_asset.md](erp_25/total_asset.md) для блока «Разработка» приведены варианты **min** / **likely** / **max** (пессимистичный, наиболее вероятный и оптимистичный сценарий).

---

## Расшифровка сокращений

| Сокращение | Расшифровка |
|------------|-------------|
| **ERP** | система класса ERP; в контексте проекта — **1С:ERP Управление предприятием** |
| **УП** | подсистема/конфигурация «Управление предприятием» |
| **НСИ** | нормативно-справочная информация |
| **ФТ** | функциональные требования |
| **ТРУ** | товары, работы, услуги |
| **ПЗ** | план закупок |
| **ИСУ** | информационная система управления (в т.ч. ИСУ Тендер, ИСУ Снабжение / СИП — по контексту отчётов) |
| **КИС** | корпоративная информационная система |
| **КССС** | контур централизованных справочников / кодов НСИ (интеграция с КИС КССС) |
| **КЭД.БД** | компонент КИС «КЭД», база договоров |
| **СИЗ** | средства индивидуальной защиты |
| **РНПТ** | регистрационный номер партии товара (прослеживаемость) |
| **ТН ВЭД** | товарная номенклатура внешнеэкономической деятельности |
| **ФНС** | Федеральная налоговая служба |
| **ЭДО** | электронный документооборот |
| **ЗКП** | запрос коммерческих предложений |
| **КП** | коммерческое предложение |
| **BSL** | встроенный язык 1С (анализ кода конфигурации) |
| **СКД** | система компоновки данных (отчёты) |
| **РС** | регистр сведений |
| **БП** | бизнес-процесс |
| **MXL** | макет (в т.ч. печатная форма 1С) |
| **M:N** | связь «многие ко многим» |
| **ID** | идентификатор (в т.ч. идентификатор потребности) |
| **min / likely / max** | нижняя, наиболее вероятная и верхняя оценка в чел.-днях |
| **ГМ, ГЭ, ГТ** | службы заказчика (главный механик, главный энергетик, главный технолог и др. — по маршрутам согласования) |
| **ИТ, АХО** | информационные технологии; административно-хозяйственный отдел |
| **ДХНО** | длительно неиспользуемые остатки (контекст отчётов по запасам) |
| **ЕПУ** | единое планирование и обеспечение (контекст назначений и потребности) |
| **MVP** | минимально жизнеспособная версия (минимальный объём для первого релиза) |
| **лтх** | префикс объектов/отчётов доработок в конфигурации (по текстам отчётов) |

---

## Файлы в `erp_25`

В начале списка — сводные документы:

| Файл | Назначение |
|------|------------|
| [total_asset.md](erp_25/total_asset.md) | Сводный файл оценки разработки (таблица по требованиям, min/likely/max в чел.-днях, ссылки на детальные отчёты в `1-asset_report/`). |
| [summarize.md](erp_25/summarize.md) | Сводный файл по допущениям, ограничениям, рискам и вариантам реализации (по группам ФТ). |

Детальные отчёты по пунктам требований:

| Файл | Тема (кратко) |
|------|----------------|
| [10_kategorizatsiya_nomenklatury.md](erp_25/10_kategorizatsiya_nomenklatury.md) | Категоризация номенклатуры |
| [11_normativy_zapasov.md](erp_25/11_normativy_zapasov.md) | Нормативы запасов |
| [12_vedenie_analogov.md](erp_25/12_vedenie_analogov.md) | Ведение аналогов номенклатуры |
| [13_avtopodbor_analogov.md](erp_25/13_avtopodbor_analogov.md) | Автоподбор аналогов |
| [14_zayavochnye_kampanii.md](erp_25/14_zayavochnye_kampanii.md) | Заявочные кампании |
| [15_zayavka_na_potrebnost_i_obespechenie.md](erp_25/15_zayavka_na_potrebnost_i_obespechenie.md) | Заявка на потребность и обеспечение |
| [16_korrektirovka_potrebnosti.md](erp_25/16_korrektirovka_potrebnosti.md) | Корректировка потребности |
| [17_soglasovanie_zayavki_na_potrebnost.md](erp_25/17_soglasovanie_zayavki_na_potrebnost.md) | Согласование заявки на потребность |
| [18_obrabotka_potrebnostey_i_sposob_obespecheniya.md](erp_25/18_obrabotka_potrebnostey_i_sposob_obespecheniya.md) | Обработка потребностей и способ обеспечения |
| [19_sposoby_obespecheniya.md](erp_25/19_sposoby_obespecheniya.md) | Способы обеспечения |
| [20_formirovanie_plana_potrebnosti.md](erp_25/20_formirovanie_plana_potrebnosti.md) | Формирование плана потребности |
| [21_soglasovanie_plana_potrebnosti.md](erp_25/21_soglasovanie_plana_potrebnosti.md) | Согласование плана потребности |
| [22_zayavki_na_zakupku_i_stroki_plana_zakupok.md](erp_25/22_zayavki_na_zakupku_i_stroki_plana_zakupok.md) | Заявки на закупку и строки плана закупок |
| [23_soglasovanie_zayavok_na_zakupku.md](erp_25/23_soglasovanie_zayavok_na_zakupku.md) | Согласование заявок на закупку |
| [24_formirovanie_plana_programmy_zakupok.md](erp_25/24_formirovanie_plana_programmy_zakupok.md) | План / программа закупок |
| [25_id_potrebnosti_konsolidatsiya.md](erp_25/25_id_potrebnosti_konsolidatsiya.md) | ID потребности при консолидации |
| [26_soglasovanie_plana_programmy_zakupok.md](erp_25/26_soglasovanie_plana_programmy_zakupok.md) | Согласование плана / программы закупок |
| [27_korrektirovochnye_plany_zakupok.md](erp_25/27_korrektirovochnye_plany_zakupok.md) | Корректировочные планы закупок |
| [28_formirovanie_lotov.md](erp_25/28_formirovanie_lotov.md) | Формирование лотов |
| [29_planirovanie_tenderov.md](erp_25/29_planirovanie_tenderov.md) | Планирование тендеров |
| [30_vvod_dannykh_o_pobeditele_tendera.md](erp_25/30_vvod_dannykh_o_pobeditele_tendera.md) | Данные о победителе тендера |
| [31_tendernaya_dokumentatsiya_po_shablonam.md](erp_25/31_tendernaya_dokumentatsiya_po_shablonam.md) | Тендерная документация по шаблонам |
| [32_sbor_i_analiz_predlozheniy_postavshchikov.md](erp_25/32_sbor_i_analiz_predlozheniy_postavshchikov.md) | Сбор и анализ предложений поставщиков |
| [33_zagruzka_cen_pobeditelya.md](erp_25/33_zagruzka_cen_pobeditelya.md) | Загрузка цен победителя |
| [34_zagruzka_cen_iz_vneshnih_istochnikov.md](erp_25/34_zagruzka_cen_iz_vneshnih_istochnikov.md) | Загрузка цен из внешних источников |
| [35_raschet_ceny_posledney_zakupki.md](erp_25/35_raschet_ceny_posledney_zakupki.md) | Цена последней закупки |
| [36_soglasovanie_indikativnyh_planovyh_cen_zakupki.md](erp_25/36_soglasovanie_indikativnyh_planovyh_cen_zakupki.md) | Индикативные плановые цены закупки |
| [37_generatsiya_zakazov_postavshiku.md](erp_25/37_generatsiya_zakazov_postavshiku.md) | Генерация заказов поставщику |
| [38_postuplenie_na_sklad.md](erp_25/38_postuplenie_na_sklad.md) | Поступление на склад |
| [39_zayavki_na_peremeschenie.md](erp_25/39_zayavki_na_peremeschenie.md) | Заявки на перемещение |
| [40_izmenenie_naznacheniya_potrebnosti.md](erp_25/40_izmenenie_naznacheniya_potrebnosti.md) | Изменение назначения потребности |
| [41_rassylki_uvedomleniya.md](erp_25/41_rassylki_uvedomleniya.md) | Рассылки и уведомления |
| [42_normativy_vydachi_siz.md](erp_25/42_normativy_vydachi_siz.md) | Нормативы выдачи СИЗ |
| [43_plan_potrebnosti_siz.md](erp_25/43_plan_potrebnosti_siz.md) | План потребности в СИЗ |
| [44_uchet_vydachi_siz.md](erp_25/44_uchet_vydachi_siz.md) | Учёт выдачи СИЗ |
| [45_kontrol_peremescheniy_siz.md](erp_25/45_kontrol_peremescheniy_siz.md) | Контроль перемещений СИЗ |
| [46_priznak_proslezhivaemosti_kody_tn_ved.md](erp_25/46_priznak_proslezhivaemosti_kody_tn_ved.md) | Прослеживаемость, коды ТН ВЭД |
| [47_avtomaticheskaya_proverka_rnpt_veb_servis_fns.md](erp_25/47_avtomaticheskaya_proverka_rnpt_veb_servis_fns.md) | Проверка РНПТ (веб-сервис ФНС) |
| [48_integratsiya_edo_zapolnenie_rnpt.md](erp_25/48_integratsiya_edo_zapolnenie_rnpt.md) | ЭДО и заполнение РНПТ |
| [49_kontrol_ostatkov_rnpt_po_partiyam.md](erp_25/49_kontrol_ostatkov_rnpt_po_partiyam.md) | Остатки по РНПТ по партиям |
| [50_avtomaticheskie_uvedomleniya_fns_proslezhivaemye.md](erp_25/50_avtomaticheskie_uvedomleniya_fns_proslezhivaemye.md) | Уведомления ФНС по прослеживаемым товарам |
| [51_otchety_po_analogam.md](erp_25/51_otchety_po_analogam.md) | Отчёты по аналогам |
| [52_sostoyanie_potrebnosti.md](erp_25/52_sostoyanie_potrebnosti.md) | Состояние потребности |
| [53_obespechennost_siz.md](erp_25/53_obespechennost_siz.md) | Обеспеченность СИЗ |
| [54_sostoyanie_zapasov.md](erp_25/54_sostoyanie_zapasov.md) | Состояние запасов |
| [55_plan_fakt_postupleniya.md](erp_25/55_plan_fakt_postupleniya.md) | План-факт поступления |
| [56_plan_fakt_zakupok_tenderov_postavok.md](erp_25/56_plan_fakt_zakupok_tenderov_postavok.md) | План-факт закупок, тендеров, поставок |
| [57_grafik_postavok.md](erp_25/57_grafik_postavok.md) | График поставок |
| [58_sravnitelnyy_analiz_tsen.md](erp_25/58_sravnitelnyy_analiz_tsen.md) | Сравнительный анализ цен |
| [59_analiz_tru_365_dney.md](erp_25/59_analiz_tru_365_dney.md) | Анализ ТРУ за 365 дней |
| [60_integratsiya_s_erp.md](erp_25/60_integratsiya_s_erp.md) | Интеграция с ERP |
| [61_integratsiya_isu_tender.md](erp_25/61_integratsiya_isu_tender.md) | Интеграция с ИСУ Тендер |
| [62_integratsiya_isu_snabzhenie.md](erp_25/62_integratsiya_isu_snabzhenie.md) | Интеграция с ИСУ Снабжение |
| [63_integratsiya_kis_ksss.md](erp_25/63_integratsiya_kis_ksss.md) | Интеграция с КИС КССС |
| [64_integratsiya_kis_ked_bd.md](erp_25/64_integratsiya_kis_ked_bd.md) | Интеграция с КИС КЭД.БД |

Подробные оценки и файлы допущений в другом дереве каталога см. в ссылках внутри [total_asset.md](erp_25/total_asset.md) и [summarize.md](erp_25/summarize.md) (пути вида `1-asset_report/…`).
