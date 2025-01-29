##biblioteca de comandos basicos 

SELECT
   0 s_0,
   "SIGEO - Fluxo Documentos"."Anos"."Ano Referência" s_1,
   "SIGEO - Fluxo Documentos"."Eventos"."Código Evento" s_2,
   "SIGEO - Fluxo Documentos"."UG Documento"."Código UG Documento" s_3,
   "SIGEO - Fluxo Documentos"."FLUXO DOCUMENTOS"."Valor NL" s_4,
   REPORT_SUM("SIGEO - Fluxo Documentos"."FLUXO DOCUMENTOS"."Valor NL" BY "SIGEO - Fluxo Documentos"."Anos"."Ano Referência") s_5
FROM "SIGEO - Fluxo Documentos"
WHERE
(("Eventos"."Código Evento" LIKE '60%') AND ("Anos"."Ano Referência" BETWEEN '2012' AND '2024') AND ("UG Documento"."Código UG Documento" IN ('081101', '081102')))
ORDER BY 2 ASC NULLS LAST
FETCH FIRST 10000001 ROWS ONLY
