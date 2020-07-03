sudo -u postgres psql

\connect datadb

CREATE TABLE medic_hypertable (
  time        	TIMESTAMPTZ       NOT NULL,
  kit_id    	TEXT              NOT NULL,
  pres_card	DOUBLE PRECISION  NULL,
  frec_resp 	DOUBLE PRECISION  NULL,
  temp_corp	DOUBLE PRECISION  NULL,
  caidas 	DOUBLE PRECISION  NULL);


INSERT INTO medic_hypertable(time, kit_id,    pres_card,	frec_resp, temp_corp,	caidas)VALUES (NOW(), 'AA001', 70.0, 50.0,40.0,35.0);