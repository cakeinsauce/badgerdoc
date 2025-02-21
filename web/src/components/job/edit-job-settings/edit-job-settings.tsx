import React, { FC } from 'react';
import { Category, Pipeline, Taxonomy, User } from 'api/typings';
import { JobValues } from 'connectors/edit-job-connector/edit-job-connector';
import AutomaticJob from '../automatic-job/automatic-job';
import styles from './edit-job-settings.module.scss';
import AutomaticManualJob from '../automatic-manual-job/automatic-manual-job';
import { JobType } from 'api/typings/jobs';
import { InfoIcon } from '../../../shared/components/info-icon/info-icon';

import { MultiSwitch } from '@epam/loveship';
import { ILens } from '@epam/uui';

export type EditJobSettingsProps = {
    pipelines: Pipeline[] | undefined;
    categories: Category[] | undefined;
    users: User[] | undefined;
    taxonomies: Taxonomy[] | undefined;
    lens: ILens<JobValues>;
    initialType?: JobType;
    showNoExtractionTab?: boolean;
};

const EditJobSettings: FC<EditJobSettingsProps> = ({
    pipelines,
    categories,
    users,
    taxonomies,
    lens,
    initialType,
    showNoExtractionTab
}) => {
    const currentJobType = lens.prop('jobType').get();
    let job;

    if (currentJobType === 'ExtractionJob') {
        job = <AutomaticJob pipelines={pipelines} lens={lens} />;
    } else if (
        currentJobType == 'ExtractionWithAnnotationJob' ||
        currentJobType == 'AnnotationJob'
    ) {
        job = (
            <AutomaticManualJob
                categories={categories}
                users={users}
                pipelines={pipelines}
                taxonomies={taxonomies}
                lens={lens}
            />
        );
    } else {
        job = (
            <>
                <p>Extraction is needed for extracting data from documents.</p>
                <p>You will be able to create extraction later.</p>
            </>
        );
    }

    const tabs = [
        {
            id: 'ExtractionJob',
            caption: 'Extraction',
            isDisabled:
                initialType === 'ExtractionWithAnnotationJob' || initialType === 'AnnotationJob'
        },
        {
            id: 'ExtractionWithAnnotationJob',
            caption: 'Extraction and annotation'
        }
    ];
    if (showNoExtractionTab) {
        tabs.unshift({
            id: 'NoExtraction',
            caption: 'No extraction'
        });
    }

    return (
        <div className={`${styles.container} flex flex-col`}>
            <div className={styles.tabs}>
                <MultiSwitch
                    size="42"
                    items={tabs}
                    {...lens.prop('jobType').toProps()}
                    value={currentJobType}
                />
                <InfoIcon
                    title="Select annotation type"
                    description={
                        <ol>
                            <li>
                                Manual annotation - manual page annotation using annotators and
                                validators.
                            </li>
                            <li>
                                Automatic Extraction - page annotation automatically using a
                                pipeline.
                            </li>
                            <li>
                                Automatic + Manual Annotation - first, the document is automatically
                                annotated, after that annotators and validators manually annotate
                                the same document.
                            </li>
                        </ol>
                    }
                />
            </div>
            <div className={`form-wrapper`}>{job}</div>
        </div>
    );
};

export default EditJobSettings;
