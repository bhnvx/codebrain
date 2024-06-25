from sqlalchemy import VARCHAR, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

from geoalchemy2 import Geometry


Base = declarative_base()


class TABLE_TL_SPBD_BULD_28000(Base):
    __tablename__ = "tl_spbd_buld_28000"
    __table_args__ = {"schema": "public"}

    id = Column(Integer(), primary_key=True, nullable=False)
    geom = Column(Geometry("MULTIPOLYGON", srid=5179))
    bdtyp_cd = Column(VARCHAR(5))
    bd_mgt_sn = Column(VARCHAR(25))
    bsi_int_sn = Column(Integer())
    bsi_zon_no = Column(VARCHAR(5))
    buld_mnnm = Column(Integer())
    buld_nm = Column(VARCHAR(100))
    buld_nm_dc = Column(VARCHAR(100))
    buld_se_cd = Column(VARCHAR(1))
    buld_slno = Column(Integer())
    bul_dpn_se = Column(VARCHAR(1))
    bul_eng_nm = Column(VARCHAR(100))
    bul_man_no = Column(Integer())
    emd_cd = Column(VARCHAR(3))
    eqb_man_sn = Column(Integer())
    gro_flo_co = Column(Integer())
    li_cd = Column(VARCHAR(2))
    lnbr_mnnm = Column(Integer())
    lnbr_slno = Column(Integer())
    mntn_yn = Column(VARCHAR(1))
    mvmn_de = Column(VARCHAR(8))
    mvmn_resn = Column(VARCHAR(100))
    mvm_res_cd = Column(VARCHAR(10))
    ntfc_de = Column(VARCHAR(8))
    opert_de = Column(VARCHAR(14))
    pos_bul_nm = Column(VARCHAR(40))
    rds_man_no = Column(Integer())
    rds_sig_cd = Column(VARCHAR(5))
    rn_cd = Column(VARCHAR(7))
    sig_cd = Column(VARCHAR(5))
    und_flo_co = Column(Integer())
