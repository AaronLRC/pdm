sudo -u postgres psql

\connect django


CREATE TABLE api_medic_kit_per_user 
( 
   kit_id TEXT PRIMARY KEY,
   user_id INTEGER REFERENCES auth_user,
   estado_comunicacion JSON,
   estado_baterias JSON,
   tiempo_muestreo JSON
);


INSERT INTO public.api_medic_kit_per_user(
	kit_id, user_id, estado_comunicacion, estado_baterias, tiempo_muestreo)
	VALUES ('AA0001', 
			1, 
			'{"estado":"conectado y enviando data"}',
			'{"medikit":"80%","mediband":"40%"}',
			'{"t_pres_card":150,"t_frec_resp":20,"t_temp_corp":1}'
		   );