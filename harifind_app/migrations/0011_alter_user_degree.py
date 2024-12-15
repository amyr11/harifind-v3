# Generated by Django 5.1.4 on 2024-12-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harifind_app', '0010_user_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='degree',
            field=models.CharField(blank=True, choices=[('CED_BECEd', 'Bachelor of Early Childhood Education (BECEd)'), ('CED_BEEd_PSE', 'Bachelor of Elementary Education with Specialization in Pre-School Education (BEEd-PSE)'), ('CED_BPE_SPE', 'Bachelor of Physical Education major in School Physical Education (BPE-SPE)'), ('CED_BSEd_Eng', 'Bachelor of Secondary Education with Specialization in English (BSEd Eng)'), ('CED_BSEd_Fil', 'Bachelor of Secondary Education with Specialization in Filipino (BSEd Fil)'), ('CED_BSEd_Math', 'Bachelor of Secondary Education with Specialization in Mathematics (BSEd Math)'), ('CED_BSEd_Sci', 'Bachelor of Secondary Education with Specialization in Science (BSEd Sci)'), ('CED_BSEd_SS', 'Bachelor of Secondary Education major in Social Studies (BSEd SS)'), ('SOG_BPA', 'Bachelor of Public Administration (BPA)'), ('PROFESSIONAL_LAWS', 'Bachelor of Laws (now Juris Doctor)'), ('PROFESSIONAL_MEDICINE', 'Doctor of Medicine'), ('PROFESSIONAL_MA_EDUCATION', 'Master of Arts in Education: Educational Administration, Social Studies, Biological Sciences, and Physical Sciences'), ('PROFESSIONAL_MA_PSYCHOLOGY', 'Master of Arts in Psychology: Industrial Psychology, and Clinical Psychology'), ('PROFESSIONAL_MA_COMMUNICATION', 'Master of Arts in Communication Management'), ('PROFESSIONAL_MA_PRINCIPALSHIP', 'Master of Arts in School Principalship'), ('PROFESSIONAL_M_FAMILY_SCIENCE', 'Master in Family Science'), ('PROFESSIONAL_MS_MATH_EDUCATION', 'Master of Science in Mathematics Education'), ('PROFESSIONAL_EDD_EDUCATIONAL_ADMIN', 'Doctor of Education in Educational Administration'), ('PROFESSIONAL_ME_ENGINEERING', 'Master of Engineering - with Specializations in: Structural Engineering, Computer Engineering, and Construction Management'), ('PROFESSIONAL_MS_ICT', 'Master of Science in Information and Communications Technology'), ('PROFESSIONAL_MS_MANAGEMENT_ENGINEERING', 'Master of Science in Management Engineering'), ('PROFESSIONAL_MA_NURSING', 'Master of Arts in Nursing'), ('PROFESSIONAL_M_LAWS', 'Master of Laws'), ('PROFESSIONAL_BBM_MBA', 'Bachelor of Business Management-Master in Business Administration'), ('PROFESSIONAL_MBA', 'Master in Business Administration'), ('PROFESSIONAL_MBA_TOP_EXEC', 'Master in Business Administration-Top Executive Program'), ('PROFESSIONAL_M_GOVERNMENT_MANAGEMENT', 'Master in Government Management'), ('PROFESSIONAL_M_GOVERNMENT_MANAGEMENT_EXEC', 'Master in Government Management-Executive Special Program'), ('PROFESSIONAL_DBA', 'Doctor of Business Administration'), ('PROFESSIONAL_DPM', 'Doctor of Public Management'), ('PROFESSIONAL_MA_SPECIAL_EDUCATION', 'Master of Arts in Special Education - Specializing in Development Delays'), ('CAUP_BS_ARCH', 'Bachelor of Science in Architecture (BS Arch)'), ('PLM_BS_BSA', 'Bachelor of Science in Accountancy (BSA)'), ('PLM_BS_BSBA_FM', 'Bachelor of Science in Business Administration major in Financial Management (BSBA FM)'), ('PLM_BS_BSBA_MM', 'Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)'), ('PLM_BS_BSBA_OM', 'Bachelor of Science in Business Administration major in Operations Management (BSBA OM)'), ('PLM_BS_BSBA_HRM', 'Bachelor of Science in Business Administration major in Human Resource Management (BSBA HRM)'), ('PLM_BS_BSBA_BE', 'Bachelor of Science in Business Administration major in Business Economics (BSBA BE)'), ('PLM_BS_BS_ENTRE', 'Bachelor of Science in Entrepreneurship (BS ENTRE)'), ('PLM_BS_BSREM', 'Bachelor of Science in Real Estate Management (BSREM)'), ('PLM_BS_BSHM', 'Bachelor of Science in Hospitality Management (BSHM)'), ('PLM_BS_BSTM', 'Bachelor of Science in Tourism Management (BSTM)'), ('CET_BSCHE', 'Bachelor of Science in Chemical Engineering (BSCHE)'), ('CET_BSCE', 'Bachelor of Science in Civil Engineering (BSCE)'), ('CET_BSCPE', 'Bachelor of Science in Computer Engineering (BSCpE)'), ('CET_BSEE', 'Bachelor of Science in Electrical Engineering (BSEE)'), ('CET_BSECE', 'Bachelor of Science in Electronics Engineering (BSECE)'), ('CET_BSME', 'Bachelor of Science in Mechanical Engineering (BSME)'), ('CET_BSMFGE', 'Bachelor of Science in Manufacturing Engineering (BSMfgE)'), ('CISTM_BSCS', 'Bachelor of Science in Computer Science (BSCS)'), ('CISTM_BSIT', 'Bachelor of Science in Information Technology (BSIT)'), ('CHASS_BAC', 'Bachelor of Arts in Communication (BAC)'), ('CHASS_BSSW', 'Bachelor of Science in Social Work (BSSW)'), ('CHASS_BMMP', 'Bachelor of Music in Music Performance (BMMP)'), ('CN_BSN', 'Bachelor of Science in Nursing (BSN)'), ('CPT_BSPT', 'Bachelor of Science in Physical Therapy (BSPT)'), ('CS_BSBIO', 'Bachelor of Science in Biology (BSBio)'), ('CS_BSMATH', 'Bachelor of Science in Mathematics (BSMath)'), ('CS_BSCHEM', 'Bachelor of Science in Chemistry (BSChem)'), ('CS_BSPSY', 'Bachelor of Science in Psychology (BSPsy)')], max_length=255, null=True),
        ),
    ]
