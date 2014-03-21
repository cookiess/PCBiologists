#mysql -u root pbi_locality < Membracidae_counts_test.sql -p > Membracidae_counts.txt

SELECT count(S1.SpecimenUID),T5.TaxName,T3.TaxName,T1.TaxName,T2.TaxName,T5.MNLUID,T3.MNLUID,T1.MNLUID,T2.MNLUID FROM Specimen S1 left join MNL T1 ON S1.Genus=T1.MNLUID left join MNL T2 ON S1.Species=T2.MNLUID left join MNL T3 ON S1.Tribe=T3.MNLUID left join MNL T4 on S1.Subfamily=T4.MNLUID left join MNL T5 on T4.ParentID=T5.MNLUID left join Locality L1 on S1.Locality=L1.LocalityUID left join Flora_MNL F1 ON S1.HostG=F1.HostMNLUID left join Flora_MNL F2 ON S1.HostSp=F2.HostMNLUID left join Flora_MNL F3 ON S1.HostSSp=F3.HostMNLUID left join Flora_MNL F4 ON S1.HostF=F4.HostMNLUID left join SubDiv SD on L1.SubDivUID=SD.SubDivUID left join StateProv SP on SD.StateProvUID=SP.StateProvUID left join colevent CE on S1.ColEventUID=CE.ColEventUID left join Collector C1 on CE.Collector=C1.CollectorUID left join Country CN on SP.CountryUID=CN.UID left join HostCommonName HC on S1.HostCName=HC.CommonUID  WHERE S1.Insect_ID=1 AND T5.MNLUID = '40537' GROUP BY T2.MNLUID;